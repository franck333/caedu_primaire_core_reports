# -*- coding: utf-8 -*-
##############################################################################
#    FullSoft, Cameroon Education
#    KSL
##############################################################################

from openerp import models, fields, api
import logging

# import subprocess
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class CaeduEleveInsolvable(models.TransientModel):
    _inherit = 'caedu.eleve.insolvable'
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_eleve_insolvable_template')
         
        return resultat
    
    @api.multi
    def invoice_print_2(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_eleve_insolvable_total_template')
         
        return resultat
