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


class CaeduEtudePvAnnuel(models.TransientModel):
    _inherit = 'caedu.etude.pv.annuel'
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_etude_pv_annuel_template')
         
        return resultat