Sub coll_action_to_DB(in_acct As String)
Dim cn As ADODB.Connection
    Set cn = New ADODB.Connection
    Dim rs As ADODB.Recordset
    strOpen = "DRIVER={Oracle in OraClient11g_home1};" & _
            "User ID=" & getLogin & _
            ";Password=" & getPasswd & _
            ";Persist Security Info=True;Data Source=DWH" & _
            ";QTO=F"
    On Error GoTo CnErrorHandler
    cn.Open strOpen
    
    Set rs = New ADODB.Recordset
    
    un = CreateObject("WScript.Network").UserName
    
    Dim cmd As New ADODB.Command
   
    cmd.CommandText = "sxema.pkg.procedure"
    cmd.ActiveConnection = cn
    cmd.CommandType = adCmdStoredProc
    Dim param1 As New ADODB.Parameter
    Dim param2 As New ADODB.Parameter
    Dim param3 As New ADODB.Parameter
    Dim param4 As New ADODB.Parameter
    Dim param5 As New ADODB.Parameter
    Dim param6 As New ADODB.Parameter
    If in_acct = "cookie" Then
        Set param1 = cmd.CreateParameter("in_object", adVarChar, adParamInput, Len(WsCooke_IP.CB_Cookie.Text), WsCooke_IP.CB_Cookie.Text)
    Else
        Set param1 = cmd.CreateParameter("in_object", adVarChar, adParamInput, Len(WsCooke_IP.CB_ip.Text), WsCooke_IP.CB_ip.Text)
    End If
    Set param2 = cmd.CreateParameter("in_type_add", adVarChar, adParamInput, Len(in_acct), in_acct)
    Set param3 = cmd.CreateParameter("in_type_src", adVarChar, adParamInput, Len(WsCooke_IP.CB_src.Text), WsCooke_IP.CB_src.Text)
    Set param4 = cmd.CreateParameter("in_val_src", adVarChar, adParamInput, Len(WsCooke_IP.TextBox1.Text), WsCooke_IP.TextBox1.Text)
    Set param5 = cmd.CreateParameter("in_user", adVarChar, adParamInput, Len(getusername), getusername)
    If in_acct = "cookie" Then
        Set param6 = cmd.CreateParameter("in_desc", adVarChar, adParamInput, Len(WsCooke_IP.TB_Cookie.Text), WsCooke_IP.TB_Cookie.Text)
    Else
        Set param6 = cmd.CreateParameter("in_desc", adVarChar, adParamInput, Len(WsCooke_IP.TB_Desc_ip.Text), WsCooke_IP.TB_Desc_ip.Text)
    End If
    cmd.Parameters.Append param1
    cmd.Parameters.Append param2
    cmd.Parameters.Append param3
    cmd.Parameters.Append param4
    cmd.Parameters.Append param5
    cmd.Parameters.Append param6
    Set rs = cmd.Execute
    If Not rs.EOF Then
        'set_cb_ip_cookie (rs.GetRows)
        'v_out = rs.GetRows
        MsgBox rs.GetString, vbInformation
        'MsgBox "Поиск окончен," & Chr(10) & " результат можно выбрать из выпадающих списков" & Chr(10) & " Cookie и IP адреса", vbInformation
        Exit Sub
    End If
    'MsgBox "Запрос вернул нулевой результат.", vbCritical
    'End
    Exit Sub
CnErrorHandler:
    Dim StrErr As String
    StrErr = "Ошибка Oracle!!!" & Chr(10)
    For Each ADOErr In cn.Errors
        'Debug.Print ADOErr.Number
        'Debug.Print ADOErr.Description
        StrErr = StrErr & ADOErr.Number & " -> " & ADOErr.Description & Chr(10)
    Next
    Debug.Print StrErr
    MsgBox StrErr, vbCritical
    End
End Sub
