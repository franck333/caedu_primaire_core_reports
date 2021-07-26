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


class CaeduPvSequentiel(models.TransientModel):
    _inherit = 'caedu.pv.sequentiel'
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_pv_sequentiel_template')
         
        return resultat
    
    
    # methode d impression 
    @api.multi
    def invoice_print2(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_fiche_report_notes_cours_ancien_template')
         
        return resultat
