# -*- coding: utf-8 -*-
##############################################################################
#    FullSoft, Cameroon Education
#    MJP
##############################################################################

from openerp import models, fields, api
import logging

# import subprocess
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class CaeduEtudeRapportPedagogiqueAnnuel(models.TransientModel):
    _inherit = 'caedu.etude.rapport.pedagogique.annuel'
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.caedu_etude_rapport_pedagogique_annuel_template')
         
        return resultat