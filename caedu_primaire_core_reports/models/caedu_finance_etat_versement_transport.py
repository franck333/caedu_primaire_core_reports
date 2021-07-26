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


class CaeduFinanceEtatVersementTransport(models.Model):
    _inherit = 'caedu.finance.etat.versement.transport'
    
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_finance_etat_versement_transport_template')
         
        return resultat
    
