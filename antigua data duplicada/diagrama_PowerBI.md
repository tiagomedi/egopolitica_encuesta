erDiagram

    ENCUESTADO {
        int Id_Encuesta PK
        int N_Encuesta
        string encuesta_a
        string encuesta_m
        string zona_u_r
        string region
        string Sexo
        int Edad
        int estrato
        string iden_pol_3
    }

    PERCEPCIONES {
        int Id_Encuesta FK
        int percepcion_1_a
        int percepcion_1_b
        int percepcion_1_c
        int percepcion_2
        int percepcion_3
        int percepcion_4
        int percepcion_5
        int percepcion_6
        int percepcion_38
        int percepcion_39
    }

    EVALUACIONES_POLITICAS {
        int Id_Encuesta FK
        int eval_gob_1
        int eval_act_pol_1_p
        int eval_act_pol_1_fh
        int eval_act_pol_1_dv
        int eval_act_pol_1_co
        int eval_act_pol_1_ca
        int eval_act_pol_1_ae
        int eval_act_pol_1_er
        int eval_act_pol_1_gt
        int eval_act_pol_17
        int eval_act_pol_18
        int pp_congreso_61_b
    }

    CONFIANZA_INSTITUCIONES {
        int Id_Encuesta FK
        int confianza_6_aa
        int confianza_6_j
        int confianza_6_i
        int confianza_6_k
    }

    DEMOCRACIA {
        int Id_Encuesta FK
        int democracia_21
    }

    BIENESTAR {
        int Id_Encuesta FK
        int bienestar_2
        int bienestar_7_a
        int bienestar_7_d
        int bienestar_7_f
        int bienestar_7_g
    }

    ESTALLIDO_SOCIAL {
        int Id_Encuesta FK
        int estallido_17
        int MBP20a
        int MBP20b
        int MBP20c
        int MBP20d
        int MBP20e
        int MBP20g
        int MBP20h
        int MBP20j
    }

    ENCUESTADO ||--o{ PERCEPCIONES : "Id_Encuesta"
    ENCUESTADO ||--o{ EVALUACIONES_POLITICAS : "Id_Encuesta"
    ENCUESTADO ||--o{ CONFIANZA_INSTITUCIONES : "Id_Encuesta"
    ENCUESTADO ||--o{ DEMOCRACIA : "Id_Encuesta"
    ENCUESTADO ||--o{ BIENESTAR : "Id_Encuesta"
    ENCUESTADO ||--o{ ESTALLIDO_SOCIAL : "Id_Encuesta"
