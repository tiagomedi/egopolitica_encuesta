import pandas as pd

df = pd.read_csv("NEW_CSV_TOTAL.csv")

# Crear las distintas tablas
encuestado = df[["Id_Encuesta", "N_Encuesta", "encuesta_a", "encuesta_m", "zona_u_r", "region", "Sexo", "Edad", "estrato", "iden_pol_3"]]
percepciones = df[["Id_Encuesta", "percepcion_1_a","percepcion_1_b","percepcion_1_c","percepcion_2","percepcion_3","percepcion_4","percepcion_5","percepcion_6","percepcion_38","percepcion_39"]]
evaluaciones = df[["Id_Encuesta","eval_gob_1","eval_act_pol_1_p","eval_act_pol_1_fh","eval_act_pol_1_dv","eval_act_pol_1_co","eval_act_pol_1_ca","eval_act_pol_1_ae","eval_act_pol_1_er","eval_act_pol_1_gt","eval_act_pol_17","eval_act_pol_18","pp_congreso_61_b"]]
confianza = df[["Id_Encuesta","confianza_6_aa","confianza_6_j","confianza_6_i","confianza_6_k"]]
democracia = df[["Id_Encuesta","democracia_21"]]
bienestar = df[["Id_Encuesta","bienestar_2","bienestar_7_a","bienestar_7_d","bienestar_7_f","bienestar_7_g"]]
estallido = df[["Id_Encuesta","estallido_17","MBP20a","MBP20b","MBP20c","MBP20d","MBP20e","MBP20g","MBP20h","MBP20j"]]

# Guardar las tablas
encuestado.to_csv("Encuestado.csv", index=False)
percepciones.to_csv("Percepciones.csv", index=False)
evaluaciones.to_csv("Evaluaciones_Politicas.csv", index=False)
confianza.to_csv("Confianza_Instituciones.csv", index=False)
democracia.to_csv("Democracia.csv", index=False)
bienestar.to_csv("Bienestar.csv", index=False)
estallido.to_csv("Estallido_Social.csv", index=False)
print("Tablas exportadas correctamente.")