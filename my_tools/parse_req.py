# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:03:44 2023

@author: User
"""

# =============================================================================
#   {
#     "Out": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\n    <soap:Body>\n        <MatchResponse xmlns=\"http://www.mclsoftware.co.uk/HunterII/WebServices\">\n            <MatchResult>&lt;ResultBlock&gt;&#13;\n    &lt;MatchSummary matches=\"0\"&gt;&#13;\n        &lt;TotalMatchScore&gt;0&lt;/TotalMatchScore&gt;&#13;\n        &lt;MatchSchemes schemeCount=\"1\"&gt;&#13;\n            &lt;Scheme&gt;&#13;\n                &lt;SchemeID&gt;DEF&lt;/SchemeID&gt;&#13;\n                &lt;Score&gt;1259&lt;/Score&gt;&#13;\n            &lt;/Scheme&gt;&#13;\n            &lt;Scheme&gt;&#13;\n                &lt;SchemeID&gt;POS&lt;/SchemeID&gt;&#13;\n                &lt;Score&gt;941&lt;/Score&gt;&#13;\n            &lt;/Scheme&gt;&#13;\n            &lt;Scheme&gt;&#13;\n                &lt;SchemeID&gt;MFO&lt;/SchemeID&gt;&#13;\n                &lt;Score&gt;999&lt;/Score&gt;&#13;\n            &lt;/Scheme&gt;&#13;\n        &lt;/MatchSchemes&gt;&#13;\n        &lt;Rules totalRuleCount=\"1\"&gt;&#13;\n            &lt;Rule ruleCount=\"1\"&gt;&#13;\n                &lt;RuleID&gt;NHOD_MA_PASS_RISK_1&lt;/RuleID&gt;&#13;\n                &lt;Score&gt;0&lt;/Score&gt;&#13;\n            &lt;/Rule&gt;&#13;\n        &lt;/Rules&gt;&#13;\n    &lt;/MatchSummary&gt;&#13;\n&lt;/ResultBlock&gt;&#13;\n</MatchResult>\n        </MatchResponse>\n    </soap:Body>\n</soap:Envelope>\n",
#     "Err": "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n                                 Dload  Upload   Total   Spent    Left  Speed\n\n  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0\n100 13834    0     0  100 13834      0  11040  0:00:01  0:00:01 --:--:-- 11040\n100 15337  100  1503  100 13834   1095  10083  0:00:01  0:00:01 --:--:-- 11178\n",
#     "Cmd": "/opt/cprocsp/bin/amd64/curl -X POST -kl https://nhod-test.bki-okb.com/OnlineMatchingCore/OnlineMatching.asmx -H \"Content-Type: text/xml\" -H \"SOAPAction:\" -E 2fc4461b7e9705acc998203bf19df8296e252861 -d '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:web=\"http://www.mclsoftware.co.uk/HunterII/WebServices\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <web:Match>\n         <!--Optional:-->\n         <web:controlXml>&lt;ControlBlock xsi:schemaLocation=&quot;urn:mclsoftware.co.uk:hunterII control.xsd&quot; xmlns=&quot;urn:mclsoftware.co.uk:hunterII&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;&gt;\n  &lt;Customer&gt;\n    &lt;CustomerID&gt;99&lt;/CustomerID&gt;\n    &lt;CustomerName&gt;452&lt;/CustomerName&gt;\n  &lt;/Customer&gt;\n  &lt;Loading&gt;\n    &lt;SubmissionLoad&gt;1&lt;/SubmissionLoad&gt;\n    &lt;SuppressVersion flag=&quot;0&quot; /&gt;\n  &lt;/Loading&gt;\n  &lt;Matching&gt;\n    &lt;MatchScheme&gt;\n      &lt;SchemeID&gt;1&lt;/SchemeID&gt;\n    &lt;/MatchScheme&gt;\n    &lt;PersistMatches&gt;1&lt;/PersistMatches&gt;\n    &lt;WorklistInsert&gt;0&lt;/WorklistInsert&gt;\n  &lt;/Matching&gt;\n  &lt;Results&gt;\n    &lt;RsltCode&gt;1&lt;/RsltCode&gt;\n  &lt;/Results&gt;\n&lt;/ControlBlock&gt;</web:controlXml>\n         <!--Optional:-->\n     <web:batchXml>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&lt;BATCH xmlns=&quot;urn:mclsoftware.co.uk:hunterII&quot;&gt;\n    &lt;HEADER&gt;\n        &lt;COUNT&gt;1&lt;/COUNT&gt;\n        &lt;ORIGINATOR&gt;452&lt;/ORIGINATOR&gt;\n        &lt;SUPPRESS&gt;Y&lt;/SUPPRESS&gt;\n    &lt;/HEADER&gt;\n    &lt;SUBMISSIONS&gt;\n        &lt;SUBMISSION&gt;\n            &lt;IDENTIFIER&gt;connectivity_test&lt;/IDENTIFIER&gt;\n            &lt;PRODUCT&gt;OD&lt;/PRODUCT&gt;\n            &lt;CLASSIFICATION&gt;LM&lt;/CLASSIFICATION&gt;\n            &lt;DATE&gt;2018-05-04&lt;/DATE&gt;\n            &lt;APP_DATE&gt;2018-04-27&lt;/APP_DATE&gt;\n            &lt;APPLICATION_VALUE&gt;691758&lt;/APPLICATION_VALUE&gt;\n            &lt;INITIAL_PAYMENT&gt;138351&lt;/INITIAL_PAYMENT&gt;\n            &lt;GUARANTY&gt;Y&lt;/GUARANTY&gt;\n            &lt;PRODUCT_TYPE&gt;3&lt;/PRODUCT_TYPE&gt;\n            &lt;APP_CHANNEL&gt;4&lt;/APP_CHANNEL&gt;\n            &lt;SALPROJECT&gt;N&lt;/SALPROJECT&gt;\n            &lt;SECSALES&gt;N&lt;/SECSALES&gt;\n            &lt;APP_NUMBER&gt;559347&lt;/APP_NUMBER&gt;\n            &lt;REASON_CODE&gt;3&lt;/REASON_CODE&gt;\n            &lt;GDS_CNT&gt;5&lt;/GDS_CNT&gt;\n            &lt;MG_PRICE&gt;4014&lt;/MG_PRICE&gt;\n            &lt;TPA_DEF&gt;N&lt;/TPA_DEF&gt;\n            &lt;FPA_DEF&gt;N&lt;/FPA_DEF&gt;\n            &lt;CR_ACT&gt;Y&lt;/CR_ACT&gt;\n            &lt;MA&gt;\n                &lt;STATUS&gt;1&lt;/STATUS&gt;\n                &lt;APP_TYPE&gt;1&lt;/APP_TYPE&gt;\n                &lt;FNAME&gt;ИВАН&lt;/FNAME&gt;\n                &lt;PNAME&gt;ИВАНОВИЧ&lt;/PNAME&gt;\n                &lt;LNAME&gt;ТЕСТ&lt;/LNAME&gt;\n                &lt;DOB&gt;1963-11-07&lt;/DOB&gt;\n                &lt;DOB_OD&gt;1963-11-07&lt;/DOB_OD&gt;\n                &lt;POB&gt;Дербент&lt;/POB&gt;\n                &lt;PER_INN&gt;1111111111&lt;/PER_INN&gt;\n                &lt;PREV_FN&gt;ПЕТР&lt;/PREV_FN&gt;\n                &lt;PREV_PN&gt;ПЕТРОВИЧ&lt;/PREV_PN&gt;\n                &lt;PREV_LN&gt;ТЕСТОВЫЙ&lt;/PREV_LN&gt;\n                &lt;INC_TM&gt;111111&lt;/INC_TM&gt;\n                &lt;INC_DOC&gt;111111&lt;/INC_DOC&gt;\n                &lt;INC_ADD&gt;11111&lt;/INC_ADD&gt;\n                &lt;DIT_TYPE&gt;1&lt;/DIT_TYPE&gt;\n                &lt;INC_CALC&gt;1&lt;/INC_CALC&gt;\n                &lt;GENDER&gt;1&lt;/GENDER&gt;\n                &lt;EDUC_LVL&gt;6&lt;/EDUC_LVL&gt;\n                &lt;MARIT_ST&gt;2&lt;/MARIT_ST&gt;\n                &lt;KIDS&gt;2&lt;/KIDS&gt;&lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;&lt;AGRMNT_STDT&gt;2018-04-27&lt;/AGRMNT_STDT&gt;&lt;AGRMNT_EXPDT&gt;2018-05-02&lt;/AGRMNT_EXPDT&gt;\n                &lt;WRK_LEN&gt;83&lt;/WRK_LEN&gt;\n                &lt;ID_client&gt;11111&lt;/ID_client&gt;\n                &lt;MA_PAS&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2005-10-17&lt;/DOC_DATE&gt;\n                    &lt;DOC_CODE&gt;111111&lt;/DOC_CODE&gt;\n                &lt;/MA_PAS&gt;\n                &lt;MA_DOC&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2000-06-19&lt;/DOC_DATE&gt;\n                    &lt;DOT&gt;3&lt;/DOT&gt;\n                &lt;/MA_DOC&gt;\n                &lt;MA_SPO&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;FNAME&gt;ТЕСТОВАЯ&lt;/FNAME&gt;\n                    &lt;PNAME&gt;АЛЕКСАНДРА&lt;/PNAME&gt;\n                    &lt;LNAME&gt;АЛЕКСАНДРОВНА&lt;/LNAME&gt;\n                    &lt;DOB&gt;1958-03-04&lt;/DOB&gt;\n                    &lt;DOB_OD&gt;1958-03-04&lt;/DOB_OD&gt;&lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;&lt;AGRMNT_STDT&gt;2018-04-27&lt;/AGRMNT_STDT&gt;&lt;AGRMNT_EXPDT&gt;2018-05-02&lt;/AGRMNT_EXPDT&gt;\n                &lt;/MA_SPO&gt;\n                &lt;MA_RAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;957484&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;34&lt;/REGION&gt;\n                    &lt;CITY&gt;КОЛОМНА&lt;/CITY&gt;\n                    &lt;STREET&gt;СРЕДНЕКИРПИЧНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;83&lt;/HOUSE&gt;\n                    &lt;APART&gt;79&lt;/APART&gt;\n                &lt;/MA_RAD&gt;\n                &lt;MA_RTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74921111111&lt;/TEL_NUM&gt;\n                &lt;/MA_RTEL&gt;\n                &lt;MA_CAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;111111&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;35&lt;/REGION&gt;\n                    &lt;CITY&gt;САМАРА&lt;/CITY&gt;\n                    &lt;STREET&gt;ПОЛЯРНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;57&lt;/HOUSE&gt;\n                    &lt;APART&gt;88&lt;/APART&gt;\n                &lt;/MA_CAD&gt;\n                &lt;MA_CTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74981111111&lt;/TEL_NUM&gt;\n                &lt;/MA_CTEL&gt;\n                &lt;MA_HTEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74931111111&lt;/TEL_NUM&gt;\n                &lt;/MA_HTEL_AD&gt;\n                &lt;MA_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79611111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL&gt;\n                &lt;MA_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79881111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL&gt;\n                &lt;MA_MTEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79511111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL_AD&gt;\n                &lt;MA_EMP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;ORG_NAME&gt;ТЕСТЛОГ&lt;/ORG_NAME&gt;\n                    &lt;INN&gt;1111111111&lt;/INN&gt;\n                    &lt;JOT&gt;5&lt;/JOT&gt;\n                    &lt;INDUSTRY_AREA&gt;11&lt;/INDUSTRY_AREA&gt;\n                    &lt;DOH&gt;2017-12-23&lt;/DOH&gt;\n                &lt;/MA_EMP&gt;\n                &lt;MA_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL&gt;\n                &lt;MA_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL&gt;\n                &lt;MA_ETEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL_AD&gt;\n                &lt;MA_EAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;436037&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;46&lt;/REGION&gt;\n                    &lt;CITY&gt;ЭНГЕЛЬС&lt;/CITY&gt;\n                    &lt;STREET&gt;КРЕПЕЖНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;65&lt;/HOUSE&gt;\n                    &lt;APART&gt;87&lt;/APART&gt;\n                &lt;/MA_EAD&gt;\n                &lt;MA_EMA&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;EMAIL&gt;HUNTER@TEST.COM&lt;/EMAIL&gt;\n                &lt;/MA_EMA&gt;\n                &lt;MA_CP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;FNAME&gt;АНДРЕЙ&lt;/FNAME&gt;\n                    &lt;PNAME&gt;АНДРЕЕВИЧ&lt;/PNAME&gt;\n                    &lt;LNAME&gt;ТЕСТОВ&lt;/LNAME&gt;\n                &lt;/MA_CP&gt;\n                &lt;CP_CTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74961111111&lt;/TEL_NUM&gt;\n                &lt;/CP_CTEL&gt;\n                &lt;CP_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79131111111&lt;/TEL_NUM&gt;\n                &lt;/CP_MTEL&gt;\n                &lt;CP_EMP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;ORG_NAME&gt;АААТЕСТ&lt;/ORG_NAME&gt;\n                    &lt;INN&gt;1111111111&lt;/INN&gt;\n                    &lt;JOT&gt;8&lt;/JOT&gt;\n                    &lt;INDUSTRY_AREA&gt;6&lt;/INDUSTRY_AREA&gt;\n                &lt;/CP_EMP&gt;\n                &lt;CP_EAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;308468&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;79&lt;/REGION&gt;\n                    &lt;CITY&gt;КОМСОМОЛЬСКНААМУРЕ&lt;/CITY&gt;\n                    &lt;STREET&gt;ВЫСОЦКОГО&lt;/STREET&gt;\n                    &lt;HOUSE&gt;34&lt;/HOUSE&gt;\n                    &lt;APART&gt;45&lt;/APART&gt;\n                &lt;/CP_EAD&gt;\n                &lt;CP_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74981111111&lt;/TEL_NUM&gt;\n                &lt;/CP_ETEL&gt;\n                &lt;CP_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74911111111&lt;/TEL_NUM&gt;\n                &lt;/CP_ETEL&gt;\n            &lt;/MA&gt;\n            &lt;AG_PERS&gt;\n                &lt;STATUS&gt;1&lt;/STATUS&gt;\n                &lt;APP_TYPE&gt;2&lt;/APP_TYPE&gt;\n                &lt;AG_CODE&gt;2&lt;/AG_CODE&gt;\n                &lt;FNAME&gt;СЕМЕН&lt;/FNAME&gt;\n                &lt;PNAME&gt;СЕМЕНОВИЧ&lt;/PNAME&gt;\n                &lt;LNAME&gt;ТЕСТИРУЮЩИЙ&lt;/LNAME&gt;\n                &lt;DOB&gt;1981-12-03&lt;/DOB&gt;\n                &lt;DOB_OD&gt;1981-12-03&lt;/DOB_OD&gt;\n                &lt;PER_INN&gt;1111111111&lt;/PER_INN&gt;\n                &lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;\n                &lt;AGRMNT_STDT&gt;2018-04-25&lt;/AGRMNT_STDT&gt;\n                &lt;AGRMNT_EXPDT&gt;2018-04-30&lt;/AGRMNT_EXPDT&gt;\n                &lt;AG_IDDOC&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2013-11-04&lt;/DOC_DATE&gt;\n                &lt;/AG_IDDOC&gt;\n                &lt;AG_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;692960&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;51&lt;/REGION&gt;\n                    &lt;CITY&gt;НЕВИННОМЫССК&lt;/CITY&gt;\n                    &lt;STREET&gt;ЗАГОРНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;32&lt;/HOUSE&gt;\n                    &lt;APART&gt;43&lt;/APART&gt;\n                &lt;/AG_AD&gt;\n                &lt;AG_TEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74961111111&lt;/TEL_NUM&gt;\n                &lt;/AG_TEL&gt;\n                &lt;AG_EMA&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;EMAIL&gt;HUNTER@TEST.COM&lt;/EMAIL&gt;\n                &lt;/AG_EMA&gt;\n            &lt;/AG_PERS&gt;\n            &lt;SPOINT&gt;\n                &lt;ORG_NAME&gt;ТЕСТФАКТОРИ&lt;/ORG_NAME&gt;\n                &lt;SPNT_TYPE&gt;2&lt;/SPNT_TYPE&gt;\n                &lt;SPNT_CODE&gt;1&lt;/SPNT_CODE&gt;\n                &lt;SPNT_LOCT&gt;1&lt;/SPNT_LOCT&gt;\n                &lt;SPNT_LOCN&gt;1&lt;/SPNT_LOCN&gt;\n                &lt;SPOINT_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;597444&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;68&lt;/REGION&gt;\n                    &lt;CITY&gt;БЛАГОВЕЩЕНСК&lt;/CITY&gt;\n                    &lt;STREET&gt;ПОЛТАВСКИИ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;76&lt;/HOUSE&gt;\n                    &lt;APART&gt;13&lt;/APART&gt;\n                &lt;/SPOINT_AD&gt;\n                &lt;SPOINT_TEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79191111111&lt;/TEL_NUM&gt;\n                &lt;/SPOINT_TEL&gt;\n            &lt;/SPOINT&gt;\n        &lt;/SUBMISSION&gt;\n    &lt;/SUBMISSIONS&gt;\n&lt;/BATCH&gt;\n     </web:batchXml>\n         <!--Optional:-->\n         <web:username>C452_OM</web:username>\n         <!--Optional:-->\n         <web:password>u(?7UH24*EoT</web:password>\n      </web:Match>\n   </soapenv:Body>\n</soapenv:Envelope>'"
#   }
# =============================================================================

from html import escape,unescape
import xml.etree.ElementTree as ET
import xml.dom.minidom as mindom


test_input_str='<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:web=\"http://www.mclsoftware.co.uk/HunterII/WebServices\">\n   <soapenv:Header/>\n   <soapenv:Body>\n      <web:Match>\n         <!--Optional:-->\n         <web:controlXml>&lt;ControlBlock xsi:schemaLocation=&quot;urn:mclsoftware.co.uk:hunterII control.xsd&quot; xmlns=&quot;urn:mclsoftware.co.uk:hunterII&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;&gt;\n  &lt;Customer&gt;\n    &lt;CustomerID&gt;99&lt;/CustomerID&gt;\n    &lt;CustomerName&gt;452&lt;/CustomerName&gt;\n  &lt;/Customer&gt;\n  &lt;Loading&gt;\n    &lt;SubmissionLoad&gt;1&lt;/SubmissionLoad&gt;\n    &lt;SuppressVersion flag=&quot;0&quot; /&gt;\n  &lt;/Loading&gt;\n  &lt;Matching&gt;\n    &lt;MatchScheme&gt;\n      &lt;SchemeID&gt;1&lt;/SchemeID&gt;\n    &lt;/MatchScheme&gt;\n    &lt;PersistMatches&gt;1&lt;/PersistMatches&gt;\n    &lt;WorklistInsert&gt;0&lt;/WorklistInsert&gt;\n  &lt;/Matching&gt;\n  &lt;Results&gt;\n    &lt;RsltCode&gt;1&lt;/RsltCode&gt;\n  &lt;/Results&gt;\n&lt;/ControlBlock&gt;</web:controlXml>\n         <!--Optional:-->\n     <web:batchXml>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&lt;BATCH xmlns=&quot;urn:mclsoftware.co.uk:hunterII&quot;&gt;\n    &lt;HEADER&gt;\n        &lt;COUNT&gt;1&lt;/COUNT&gt;\n        &lt;ORIGINATOR&gt;452&lt;/ORIGINATOR&gt;\n        &lt;SUPPRESS&gt;Y&lt;/SUPPRESS&gt;\n    &lt;/HEADER&gt;\n    &lt;SUBMISSIONS&gt;\n        &lt;SUBMISSION&gt;\n            &lt;IDENTIFIER&gt;connectivity_test&lt;/IDENTIFIER&gt;\n            &lt;PRODUCT&gt;OD&lt;/PRODUCT&gt;\n            &lt;CLASSIFICATION&gt;LM&lt;/CLASSIFICATION&gt;\n            &lt;DATE&gt;2018-05-04&lt;/DATE&gt;\n            &lt;APP_DATE&gt;2018-04-27&lt;/APP_DATE&gt;\n            &lt;APPLICATION_VALUE&gt;691758&lt;/APPLICATION_VALUE&gt;\n            &lt;INITIAL_PAYMENT&gt;138351&lt;/INITIAL_PAYMENT&gt;\n            &lt;GUARANTY&gt;Y&lt;/GUARANTY&gt;\n            &lt;PRODUCT_TYPE&gt;3&lt;/PRODUCT_TYPE&gt;\n            &lt;APP_CHANNEL&gt;4&lt;/APP_CHANNEL&gt;\n            &lt;SALPROJECT&gt;N&lt;/SALPROJECT&gt;\n            &lt;SECSALES&gt;N&lt;/SECSALES&gt;\n            &lt;APP_NUMBER&gt;559347&lt;/APP_NUMBER&gt;\n            &lt;REASON_CODE&gt;3&lt;/REASON_CODE&gt;\n            &lt;GDS_CNT&gt;5&lt;/GDS_CNT&gt;\n            &lt;MG_PRICE&gt;4014&lt;/MG_PRICE&gt;\n            &lt;TPA_DEF&gt;N&lt;/TPA_DEF&gt;\n            &lt;FPA_DEF&gt;N&lt;/FPA_DEF&gt;\n            &lt;CR_ACT&gt;Y&lt;/CR_ACT&gt;\n            &lt;MA&gt;\n                &lt;STATUS&gt;1&lt;/STATUS&gt;\n                &lt;APP_TYPE&gt;1&lt;/APP_TYPE&gt;\n                &lt;FNAME&gt;ИВАН&lt;/FNAME&gt;\n                &lt;PNAME&gt;ИВАНОВИЧ&lt;/PNAME&gt;\n                &lt;LNAME&gt;ТЕСТ&lt;/LNAME&gt;\n                &lt;DOB&gt;1963-11-07&lt;/DOB&gt;\n                &lt;DOB_OD&gt;1963-11-07&lt;/DOB_OD&gt;\n                &lt;POB&gt;Дербент&lt;/POB&gt;\n                &lt;PER_INN&gt;1111111111&lt;/PER_INN&gt;\n                &lt;PREV_FN&gt;ПЕТР&lt;/PREV_FN&gt;\n                &lt;PREV_PN&gt;ПЕТРОВИЧ&lt;/PREV_PN&gt;\n                &lt;PREV_LN&gt;ТЕСТОВЫЙ&lt;/PREV_LN&gt;\n                &lt;INC_TM&gt;111111&lt;/INC_TM&gt;\n                &lt;INC_DOC&gt;111111&lt;/INC_DOC&gt;\n                &lt;INC_ADD&gt;11111&lt;/INC_ADD&gt;\n                &lt;DIT_TYPE&gt;1&lt;/DIT_TYPE&gt;\n                &lt;INC_CALC&gt;1&lt;/INC_CALC&gt;\n                &lt;GENDER&gt;1&lt;/GENDER&gt;\n                &lt;EDUC_LVL&gt;6&lt;/EDUC_LVL&gt;\n                &lt;MARIT_ST&gt;2&lt;/MARIT_ST&gt;\n                &lt;KIDS&gt;2&lt;/KIDS&gt;&lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;&lt;AGRMNT_STDT&gt;2018-04-27&lt;/AGRMNT_STDT&gt;&lt;AGRMNT_EXPDT&gt;2018-05-02&lt;/AGRMNT_EXPDT&gt;\n                &lt;WRK_LEN&gt;83&lt;/WRK_LEN&gt;\n                &lt;ID_client&gt;11111&lt;/ID_client&gt;\n                &lt;MA_PAS&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2005-10-17&lt;/DOC_DATE&gt;\n                    &lt;DOC_CODE&gt;111111&lt;/DOC_CODE&gt;\n                &lt;/MA_PAS&gt;\n                &lt;MA_DOC&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2000-06-19&lt;/DOC_DATE&gt;\n                    &lt;DOT&gt;3&lt;/DOT&gt;\n                &lt;/MA_DOC&gt;\n                &lt;MA_SPO&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;FNAME&gt;ТЕСТОВАЯ&lt;/FNAME&gt;\n                    &lt;PNAME&gt;АЛЕКСАНДРА&lt;/PNAME&gt;\n                    &lt;LNAME&gt;АЛЕКСАНДРОВНА&lt;/LNAME&gt;\n                    &lt;DOB&gt;1958-03-04&lt;/DOB&gt;\n                    &lt;DOB_OD&gt;1958-03-04&lt;/DOB_OD&gt;&lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;&lt;AGRMNT_STDT&gt;2018-04-27&lt;/AGRMNT_STDT&gt;&lt;AGRMNT_EXPDT&gt;2018-05-02&lt;/AGRMNT_EXPDT&gt;\n                &lt;/MA_SPO&gt;\n                &lt;MA_RAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;957484&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;34&lt;/REGION&gt;\n                    &lt;CITY&gt;КОЛОМНА&lt;/CITY&gt;\n                    &lt;STREET&gt;СРЕДНЕКИРПИЧНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;83&lt;/HOUSE&gt;\n                    &lt;APART&gt;79&lt;/APART&gt;\n                &lt;/MA_RAD&gt;\n                &lt;MA_RTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74921111111&lt;/TEL_NUM&gt;\n                &lt;/MA_RTEL&gt;\n                &lt;MA_CAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;111111&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;35&lt;/REGION&gt;\n                    &lt;CITY&gt;САМАРА&lt;/CITY&gt;\n                    &lt;STREET&gt;ПОЛЯРНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;57&lt;/HOUSE&gt;\n                    &lt;APART&gt;88&lt;/APART&gt;\n                &lt;/MA_CAD&gt;\n                &lt;MA_CTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74981111111&lt;/TEL_NUM&gt;\n                &lt;/MA_CTEL&gt;\n                &lt;MA_HTEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74931111111&lt;/TEL_NUM&gt;\n                &lt;/MA_HTEL_AD&gt;\n                &lt;MA_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79611111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL&gt;\n                &lt;MA_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79881111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL&gt;\n                &lt;MA_MTEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79511111111&lt;/TEL_NUM&gt;\n                &lt;/MA_MTEL_AD&gt;\n                &lt;MA_EMP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;ORG_NAME&gt;ТЕСТЛОГ&lt;/ORG_NAME&gt;\n                    &lt;INN&gt;1111111111&lt;/INN&gt;\n                    &lt;JOT&gt;5&lt;/JOT&gt;\n                    &lt;INDUSTRY_AREA&gt;11&lt;/INDUSTRY_AREA&gt;\n                    &lt;DOH&gt;2017-12-23&lt;/DOH&gt;\n                &lt;/MA_EMP&gt;\n                &lt;MA_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL&gt;\n                &lt;MA_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL&gt;\n                &lt;MA_ETEL_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74951111111&lt;/TEL_NUM&gt;\n                &lt;/MA_ETEL_AD&gt;\n                &lt;MA_EAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;436037&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;46&lt;/REGION&gt;\n                    &lt;CITY&gt;ЭНГЕЛЬС&lt;/CITY&gt;\n                    &lt;STREET&gt;КРЕПЕЖНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;65&lt;/HOUSE&gt;\n                    &lt;APART&gt;87&lt;/APART&gt;\n                &lt;/MA_EAD&gt;\n                &lt;MA_EMA&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;EMAIL&gt;HUNTER@TEST.COM&lt;/EMAIL&gt;\n                &lt;/MA_EMA&gt;\n                &lt;MA_CP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;FNAME&gt;АНДРЕЙ&lt;/FNAME&gt;\n                    &lt;PNAME&gt;АНДРЕЕВИЧ&lt;/PNAME&gt;\n                    &lt;LNAME&gt;ТЕСТОВ&lt;/LNAME&gt;\n                &lt;/MA_CP&gt;\n                &lt;CP_CTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74961111111&lt;/TEL_NUM&gt;\n                &lt;/CP_CTEL&gt;\n                &lt;CP_MTEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79131111111&lt;/TEL_NUM&gt;\n                &lt;/CP_MTEL&gt;\n                &lt;CP_EMP&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;ORG_NAME&gt;АААТЕСТ&lt;/ORG_NAME&gt;\n                    &lt;INN&gt;1111111111&lt;/INN&gt;\n                    &lt;JOT&gt;8&lt;/JOT&gt;\n                    &lt;INDUSTRY_AREA&gt;6&lt;/INDUSTRY_AREA&gt;\n                &lt;/CP_EMP&gt;\n                &lt;CP_EAD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;308468&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;79&lt;/REGION&gt;\n                    &lt;CITY&gt;КОМСОМОЛЬСКНААМУРЕ&lt;/CITY&gt;\n                    &lt;STREET&gt;ВЫСОЦКОГО&lt;/STREET&gt;\n                    &lt;HOUSE&gt;34&lt;/HOUSE&gt;\n                    &lt;APART&gt;45&lt;/APART&gt;\n                &lt;/CP_EAD&gt;\n                &lt;CP_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74981111111&lt;/TEL_NUM&gt;\n                &lt;/CP_ETEL&gt;\n                &lt;CP_ETEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74911111111&lt;/TEL_NUM&gt;\n                &lt;/CP_ETEL&gt;\n            &lt;/MA&gt;\n            &lt;AG_PERS&gt;\n                &lt;STATUS&gt;1&lt;/STATUS&gt;\n                &lt;APP_TYPE&gt;2&lt;/APP_TYPE&gt;\n                &lt;AG_CODE&gt;2&lt;/AG_CODE&gt;\n                &lt;FNAME&gt;СЕМЕН&lt;/FNAME&gt;\n                &lt;PNAME&gt;СЕМЕНОВИЧ&lt;/PNAME&gt;\n                &lt;LNAME&gt;ТЕСТИРУЮЩИЙ&lt;/LNAME&gt;\n                &lt;DOB&gt;1981-12-03&lt;/DOB&gt;\n                &lt;DOB_OD&gt;1981-12-03&lt;/DOB_OD&gt;\n                &lt;PER_INN&gt;1111111111&lt;/PER_INN&gt;\n                &lt;AGRMNT_FLG&gt;Y&lt;/AGRMNT_FLG&gt;\n                &lt;AGRMNT_STDT&gt;2018-04-25&lt;/AGRMNT_STDT&gt;\n                &lt;AGRMNT_EXPDT&gt;2018-04-30&lt;/AGRMNT_EXPDT&gt;\n                &lt;AG_IDDOC&gt;\n                    &lt;DOC_NUMBER&gt;1111111111&lt;/DOC_NUMBER&gt;\n                    &lt;DOC_DATE&gt;2013-11-04&lt;/DOC_DATE&gt;\n                &lt;/AG_IDDOC&gt;\n                &lt;AG_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;692960&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;51&lt;/REGION&gt;\n                    &lt;CITY&gt;НЕВИННОМЫССК&lt;/CITY&gt;\n                    &lt;STREET&gt;ЗАГОРНАЯ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;32&lt;/HOUSE&gt;\n                    &lt;APART&gt;43&lt;/APART&gt;\n                &lt;/AG_AD&gt;\n                &lt;AG_TEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;74961111111&lt;/TEL_NUM&gt;\n                &lt;/AG_TEL&gt;\n                &lt;AG_EMA&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;EMAIL&gt;HUNTER@TEST.COM&lt;/EMAIL&gt;\n                &lt;/AG_EMA&gt;\n            &lt;/AG_PERS&gt;\n            &lt;SPOINT&gt;\n                &lt;ORG_NAME&gt;ТЕСТФАКТОРИ&lt;/ORG_NAME&gt;\n                &lt;SPNT_TYPE&gt;2&lt;/SPNT_TYPE&gt;\n                &lt;SPNT_CODE&gt;1&lt;/SPNT_CODE&gt;\n                &lt;SPNT_LOCT&gt;1&lt;/SPNT_LOCT&gt;\n                &lt;SPNT_LOCN&gt;1&lt;/SPNT_LOCN&gt;\n                &lt;SPOINT_AD&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;COUNTRY&gt;RU&lt;/COUNTRY&gt;\n                    &lt;POST_CODE&gt;597444&lt;/POST_CODE&gt;\n                    &lt;REGION&gt;68&lt;/REGION&gt;\n                    &lt;CITY&gt;БЛАГОВЕЩЕНСК&lt;/CITY&gt;\n                    &lt;STREET&gt;ПОЛТАВСКИИ&lt;/STREET&gt;\n                    &lt;HOUSE&gt;76&lt;/HOUSE&gt;\n                    &lt;APART&gt;13&lt;/APART&gt;\n                &lt;/SPOINT_AD&gt;\n                &lt;SPOINT_TEL&gt;\n                    &lt;STATUS&gt;1&lt;/STATUS&gt;\n                    &lt;TEL_NUM&gt;79191111111&lt;/TEL_NUM&gt;\n                &lt;/SPOINT_TEL&gt;\n            &lt;/SPOINT&gt;\n        &lt;/SUBMISSION&gt;\n    &lt;/SUBMISSIONS&gt;\n&lt;/BATCH&gt;\n     </web:batchXml>\n         <!--Optional:-->\n         <web:username>C452_OM</web:username>\n         <!--Optional:-->\n         <web:password>u(?7UH24*EoT</web:password>\n      </web:Match>\n   </soapenv:Body>\n</soapenv:Envelope>'
#print(test_input_str)


xml_test_str=unescape(test_input_str)

xml_test_str2=u'''
<CAT>
  <NAME>Izzy</NAME>
  <BREED>Siamese</BREED>
  <AGE>6</AGE>
  <ALTERED>yes</ALTERED>
  <DECLAWED>no</DECLAWED>
  <LICENSE>Izz138bod</LICENSE>
  <OWNER>Colin Wilcox</OWNER>
</CAT>
'''

xml_test_str3='''<xsd:element name="CAT"></xsd:element>'''

#print(xml_test_str3)
# =============================================================================
# namespaces = {
#     'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
#     'a': 'http://www.etis.fskab.se/v1.0/ETISws',
#     'soapenv':'http://schemas.xmlsoap.org/soap/envelope/',
#     'web':'http://www.mclsoftware.co.uk/HunterII/WebServices'
# }
# dom = ET.fromstring(test_input_str)
# =============================================================================
dom_min=mindom.parseString(test_input_str)
#print(dom_min.toprettyxml())
#tags=['soapenv:Header','soapenv:Body']

#dom_min=mindom.parseString(xml_test_str2)

dom_min=mindom.parse('Data.xml')

root=dom_min

root_tag = root.documentElement.tagName

from xml.dom.minidom import Node

def getNode(tagName, i=1, tagHictory=''):
    tab_count=1
    tab_char='~'
    for elem in root.getElementsByTagName(tagName):
        for x in elem.childNodes:
            if x.nodeType == Node.ELEMENT_NODE:
                history=x.tagName if tagHictory == '' else f'{tagHictory}+{x.tagName}'
                prefix=tab_char*i*tab_count
                if len(x.childNodes) < 1 :
                    print(prefix, history, x.tagName)
                else:
                    #print(prefix, x.tagName, '=>', x.childNodes[0].data)
                    print(prefix, history, x.tagName, '=>' , x.childNodes[0].data)
                getAttrs(x, prefix)
                getNode(x.tagName, i+1,history)

def getAttrs(node, prefix=''):
    attrs = dict(node.attributes.items())
    for a in attrs:
        print(prefix, 'attrebute name:', a, 'value:', attrs[a])

def node_to_dataFrame(tree):
    for node in tree:
        
        
print(root_tag)
getAttrs(root.documentElement)                 
getNode(root_tag)


                    
# =============================================================================
# n = mindom.parseString('<n a="1" b="2" />').documentElement
# print(n.attributes.items())
# attrs = dict(n.attributes.items())
# print(attrs,type(attrs))
# for a in attrs:
#     print('name:', a, 'value:', attrs[a])
# =============================================================================



# =============================================================================
# names = dom.findall(
#     './soap:Body'
#     '/a:GetStartEndPointResponse'
#     '/a:GetStartEndPointResult'
#     '/a:StartPoints'
#     '/a:Point'
#     '/a:Name',
#     namespaces,
# )
# =============================================================================
# =============================================================================
# names=dom.findall(
#     './soapenv:Envelope'
#     './soapenv:Body',
#          namespaces,
#     )
# for name in names:
#     print(name.text)
# =============================================================================




