# -*- coding: utf-8 -*-
##############################################################################
#    FullSoft, Cameroon Medical
#    Francklin TAGNE
##############################################################################

{
    'name': 'Caedu Primaire Core Reports',
    'version': '8.0.1',
    'category': 'Education',
    'author': 'FullSoft',
    'website': 'http://www.fullsoft.cm',
    'depends': ['caedu_be', 'caedu_fe_core'],
    'data': [
        
        'views/add_css.xml',
       
        # les entetes
        'reports/entete/caedu_vision_french_entete_base.xml',
        'reports/entete/camed_custom_invoice_head2.xml',  
        'reports/entete/caedu_entete_nouvelle_version.xml',   
        'reports/entete/caedu_primaire_french_entete_recu.xml',
        'reports/entete/caedu_primaire_eng_entete_recu.xml',   
        'reports/entete/caedu_primaire_french_entete_recu_new.xml',
        'reports/entete/caedu_primaire_eng_entete_recu_new.xml',
        
        'reports/entete/caedu_primaire_mini_entete_recu_2021.xml',
        'reports/entete/caedu_primaire_mini_entete_recu_eng_2021.xml',
        
        
        
        # ----- fe core ----- 
        
        'reports/fe_core/caedu_liste_enseignants.xml',
        'reports/fe_core/caedu_classe_liste_eleves.xml',
        'reports/fe_core/caedu_classe_liste_eleves_2.xml',
        'reports/fe_core/caedu_classe_grille_note_max_evaluation.xml',
        'reports/fe_core/caedu_liste_moyenne.xml',  
        'reports/fe_core/caedu_releve_note_cours.xml', 
        'reports/fe_core/caedu_releve_note_cours_eng.xml',  
        'reports/fe_core/caedu_etude_effectif_classe.xml',   
        
        
        #'reports/fe_core/caedu_bulletin_sequentiel_test.xml',
        #'reports/fe_core/caedu_bulletin_sequentiel_anglophone_millenaire.xml',
        'reports/fe_core/caedu_bulletin_sequentiel_francophone.xml',
        'reports/fe_core/caedu_bulletin_sequentiel_anglais.xml',
        'reports/fe_core/caedu_bulletin_sequentiel_billingue.xml', 
        'reports/fe_core/caedu_bulletin_sequentiel_francophone_millenaire.xml', 
        'reports/fe_core/caedu_bulletin_sequentiel_francophone_elohim.xml',
        'reports/fe_core/caedu_bulletin_sequentiel_anglophone_elohim.xml',
        
        'reports/fe_core/caedu_bulletin_sequentiel_apc_deux_pages_new_wafo.xml',
        'reports/fe_core/caedu_bulletin_sequentiel_apc_deux_pages_new_eng_wafo.xml',
        
        'reports/fe_core/caedu_bulletin_trimestriel_francophone.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_anglophone.xml',
        'reports/fe_core/caedu_etude_bulletin_trimestriel_bilingue.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_francophone_millenaire.xml', 
        'reports/fe_core/caedu_bulletin_trimestriel_francophone_elohim.xml',   
        'reports/fe_core/caedu_bulletin_trimestriel_anglophone_elohim.xml',  
        
        'reports/fe_core/caedu_bulletin_trimestriel_apc_une_pages.xml', 
        'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_new.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_apc_une_page_complet.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_complet_new.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_new_eng.xml', 
        'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_new_wafo.xml',
        'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_new_eng_wafo.xml',
        
        #'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages.xml',
        #'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_complet.xml',  
        #'reports/fe_core/caedu_bulletin_trimestriel_apc_deux_pages_complet_eng.xml',
        
        'reports/fe_core/caedu_bulletin_annuel_francophone.xml', 
        'reports/fe_core/caedu_bulletin_annuel_anglophone.xml', 
        'reports/fe_core/caedu_etude_bulletin_annuel_bilingue.xml',
        'reports/fe_core/caedu_bulletin_annuel_francophone_elohim.xml',  
        'reports/fe_core/caedu_bulletin_annuel_francophone_millenaire.xml',  
        'reports/fe_core/caedu_bulletin_annuel_anglophone_millenaire.xml',
        'reports/fe_core/caedu_bulletin_annuel_anglophone_elohim.xml',
        'reports/fe_core/caedu_bulletin_annuel_apc_deux_pages_wafo.xml',
        'reports/fe_core/caedu_bulletin_annuel_apc_deux_pages_wafo_eng.xml',
        
        #'reports/fe_core/caedu_releve_fiche_note.xml', 
        'reports/fe_core/caedu_pv_sequentiel.xml', 
       
        'reports/fe_core/caedu_etude_releve_note_saisi.xml',
        #'reports/fe_core/caedu_pv_trimestriel.xml',
        
        #'reports/fe_core/caedu_fiche_verif_note.xml',
        #'reports/fe_core/caedu_fiche_verif_note_eng.xml',
        'reports/fe_core/caedu_etude_fiche_report_notes.xml',
        'reports/fe_core/caedu_etude_fiche_report_notes_fraternite.xml',
        'reports/fe_core/caedu_classe_fiche _report_notes_maternelle.xml',
        'reports/fe_core/caedu_etude_pv_annuel.xml',
        'reports/fe_core/caedu_etude_rapport_pedagogique_annuel.xml',
        
        
        
         
        # ----- finances ----- 
        'reports/finance/caedu_recu_inscription_cantine.xml',
        'reports/finance/caedu_recu_inscription_evenement.xml',
        'reports/finance/caedu_recu_reglement_dette.xml',
        'reports/finance/caedu_recu_achat_tenue.xml',  
        'reports/finance/caedu_finance_etat_mouvement.xml',   
        'reports/finance/caedu_finance_etat_mouvement_2.xml',
        'reports/finance/caedu_finance_etat_versement_transport.xml',
        
        'reports/finance/caedu_recu_versement_transport_une_page_2021.xml',
        'reports/finance/caedu_recu_versement_transport_une_page_eng_2021.xml',  
        'reports/finance/caedu_recu_versement_transport_deux_pages.xml',
        'reports/finance/caedu_recu_versement_transport_deux_pages_eng.xml',
          
        'reports/finance/caedu_analyse_financiere_inscriptions.xml',
        
        # ----- pension -----
        'reports/pension/caedu_recu_encaissement_une_page.xml',
        'reports/pension/caedu_recu_encaissement_new.xml',
        'reports/pension/caedu_recu_encaissement_eng_une_page.xml',
        'reports/pension/caedu_recu_encaissement_deux_pages.xml',
        'reports/pension/caedu_recu_encaissement_eng_deux_pages.xml',
        'reports/pension/caedu_recu_encaissement_deux_pages_fraternite.xml',
        'reports/pension/caedu_recu_encaissement_eng_deux_pages_fraternite.xml',
        
        #2021 DT
        'reports/pension/caedu_recu_encaissement_2021.xml',
        'reports/pension/caedu_recu_encaissement_eng_2021.xml',
        'reports/pension/caedu_recu_encaissement_2021_une_page.xml',
        
        
        'reports/pension/caedu_liste_eleves_selection.xml',
        'reports/pension/caedu_liste_eleves_selection_insolvables.xml',   
        'reports/pension/caedu_liste_eleves_insolvables_par_classe.xml',
        'reports/pension/caedu_liste_eleves_selection_retard_paiement.xml',
        'reports/pension/caedu_recu_encaissement_eng_new.xml',
        'reports/pension/caedu_recu_encaissement_deux_page_new.xml',
        'reports/pension/caedu_recu_encaissement_deux_page_eng_new.xml',    
        'reports/pension/caedu_eleve_insolvable.xml',
        'reports/pension/caedu_eleve_insolvable_total.xml',
        
       
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
