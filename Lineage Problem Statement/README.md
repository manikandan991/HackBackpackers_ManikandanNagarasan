# Next-Path
# SQl lineage problem 

python3 sql_lineage.py <sql command to check>

Sample outPut:
===========

C:\Users\manikandan.n\Desktop\demo>python sql_lineage.py "SELECT T.SWB_CNTRY_ID, T.CNTRY_TYPE_CD, T.DW_EFF_DT, S.DW_AS_OF_DT FROM (SELECT SWB_CNTRY_ID, CNTRY_TYPE_CD, RCV_IN, DW_EFF_DT, MAX(DW_EFF_DT) MAX_EFF_DT FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T WHERE CURR_IN=1 GROUP BY 1,2,3,4) T, (SELECT SWB_CNTRY_ID, CNTRY_SCHEME_CD, DW_AS_OF_DT, DW_ACTN_IND FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S WHERE S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD AND (S.DW_SCTN_IND=‘U’ OR (S.DW_ACTN_IND=‘I’ AND T.RCV_IN=0)) AND S.DW_AS_OF_DT > T.MAX_EFF_DT"


column => table
swb_cntry_id ==> idw_data.cntry_multi_def_cd_t
cntry_type_cd ==> idw_data.cntry_multi_def_cd_t
dw_eff_dt ==> idw_data.cntry_multi_def_cd_t
dw_as_of_dt ==> idw_stage.cntry_multi_def_cd_s
