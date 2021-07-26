# -*- coding: utf-8 -*-
##############################################################################
#    FullSoft, Cameroon Education
#    TMP
##############################################################################

from openerp import models, fields, api
import logging

# import subprocess
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class CaeduEtudeReleveNoteSaisi(models.TransientModel):
    _inherit = 'caedu.etude.releve.note.saisi'
    
    # methode d impression 
    @api.multi
    def invoice_print(self):
        
        # traitement sp�cifique a deido  
        resultat = self.env['report'].get_action(self, 'caedu_primaire_core_reports.report_caedu_etude_releve_note_saisi_template')
         
        return resultat
