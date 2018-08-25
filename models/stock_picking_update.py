from odoo import api, fields, models, _


class Picking_update(models.Model):
    _inherit='stock.picking'

    def utilidad(self):

        sql="""
                select sp.name, m.name, m.product_qty, pt.list_price, pt.standard_price
                from stock_picking sp
                INNER JOIN stock_move m on sp.id = m.picking_id
                INNER JOIN product_template pt on m.product_id= pt.id
                INNER JOIN product_category pc on pt.categ_id = pc.id
                WHERE sp.id={}
                AND pt.type in ('consu','product')
                AND pt.categ_id=1
            """.format(self.id)

        self.env.cr.execute(sql)
        consulta= self.env.cr.dictfetchall()
        total_utilidad=0
        for con in consulta:
            utilidad=(con['product_qty']*con['list_price'])- (con['standard_price']*con['product_qty'])
            total_utilidad=utilidad+total_utilidad

        total_gastos=0
        for con in self.gastos_instalacion():
            total_gastos= total_gastos + con['total_amount']

        #RETORNA EL VALOR CON EL SIGNO DE PESOS '$'
        return '$ '+str(total_utilidad), '$ ' + str(total_gastos)

    def estacion_impuestos(self):

        sql="""
                SELECT x_studio_field_r5v12 as n_estacion,
                ai.amount_total as precio_venta,
                ai.currency_id,
                so.tipo_cambio
                from sale_order so
                INNER JOIN account_invoice ai on so.name=ai.origin
                WHERe so.name='{}'
            """.format(self.origin)
        self.env.cr.execute(sql)
        consulta = self.env.cr.dictfetchall()

        contenido=[]
        for con in consulta:
            if con['currency_id']==3:
                if con['tipo_cambio']==0.0:
                    aux = {
                        'n_estacion': con['n_estacion'],
                        'precio_venta': str(con['precio_venta']) + ' USD',
                        'precio_venta_pesos': con['precio_venta'] * 1,
                        'tipo_cambio': con['tipo_cambio'],
                        'currency_id': con['currency_id']
                    }
                    contenido.append(aux)
                else:
                    aux={
                        'n_estacion':con['n_estacion'],
                        'precio_venta': str(con['precio_venta']) + ' USD',
                        'precio_venta_pesos':con['precio_venta'] * con['tipo_cambio'],
                        'tipo_cambio':con['tipo_cambio'],
                        'currency_id':con['currency_id']
                    }
                    contenido.append(aux)

            else:
                aux2 = {
                    'n_estacion': con['n_estacion'],
                    'precio_venta': con['precio_venta'],
                    'tipo_cambio': con['tipo_cambio'],
                    'currency_id':False,
                }
                contenido.append(aux2)


        return contenido

    def gastos_instalacion(self):

        sql="""
                select pt.name as nombre_producto,
                he.name as nombre_empleado,
                h.total_amount
                from hr_expense h
                INNER JOIN sale_order so on h.sale_order_id = so.id
                INNER JOIN product_product pp on h.product_id = pp.id
                INNER JOIN product_template pt on pp.product_tmpl_id = pt.id
                INNER JOIN hr_employee he on h.employee_id = he.id
                WHERe so.name='{}'
            """.format(self.origin)
        self.env.cr.execute(sql)
        gastos_instalacion= self.env.cr.dictfetchall()

        importe_venta=self.tasa_importe()
        for con in gastos_instalacion:
            operacion_porcentaje_gastos=(con['total_amount'] / importe_venta['precio_venta']) * 100
            con['porcentaje_gastos']=str(operacion_porcentaje_gastos)[0:len(str(operacion_porcentaje_gastos))-9]

        return gastos_instalacion

    def productos_surtidos(self):

        sql="""
                select pt.name,
                pt.standard_price,
                m.product_qty
                from stock_picking sp
                INNER JOIN stock_move m on sp.id = m.picking_id
                INNER JOIN product_product pp on m.product_id = pp.id
                INNER JOIN product_template pt on pp.product_tmpl_id = pt.id
                WHERE sp.id={}
            """.format(self.id)
        self.env.cr.execute(sql)
        consulta= self.env.cr.dictfetchall()

        total_productos_surtidos=0
        for con in consulta:
            costos_equipos = con['standard_price'] * con['product_qty']
            total_productos_surtidos= total_productos_surtidos + costos_equipos

        return '$ '+str(total_productos_surtidos)

    def tasa_importe(self):
        #SE INICIALIZA UN DICCIONARIO CON 'currency_id':False, YA QUE SI NO HAY FACTURA
        #DA ERROR POR QUE EL DICCIONARIO QUE REGRESA ESTA VACIO Y 'currency_id' SE USA PARA
        # VALIDAR EN QUE APARESCA UNA TABLA EN EL XML
        dict={'currency_id':False}

        for con in self.estacion_impuestos():
            if con['currency_id']==3:
                dict={
                    'tipo_cambio':con['tipo_cambio'],
                    'precio_venta':con['precio_venta_pesos'],
                    'currency_id':con['currency_id'],
                }

            else:
                dict = {
                    'tipo_cambio': con['tipo_cambio'],
                    'precio_venta': con['precio_venta'],
                    'currency_id': con['currency_id'],
                }

        return dict
