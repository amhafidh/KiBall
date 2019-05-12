Public Class Form1
    Dim myProcesses As Process
    Dim kuanza, kumaliza, txtDiff, thescript As String
    Dim startTime As Double
    Dim playername As String
    Dim score, age As Integer

    Dim dtmStart, dtmEnd As Date
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        My.Computer.Audio.Play("C:\Desktop\projects\game\Kevin_Rudolf_Ft_Birdman_Jay_Sean_Lil_Wayne_-_I_Mad.wav", _
        AudioPlayMode.Background)



    End Sub


       

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs)
        'System.Diagnostics.Process.Start("C:\Desktop\projects\game\timer.py")
        'System.Diagnostics.Process.Start("C:\movies\Trainwreck.2015.720p.HDRiP.999MB.ShAaNiG.mkv")

       


        'Shell("C:\Python33\python.exe C:\Desktop\projects\game\timer.py")
        'Process.Start("C:\Desktop\projects\game\timer.py")

        ' Visual Basic

        'myProcesses = Process.Start("C:\Desktop\projects\game\timer.py")

        'myProcesses = Process.GetProcessesByName("python.exe)")
        ' Tests the Responding property for a True return value.
        'If myProcesses.Count() > 0 Then
        'If myProcesses(0).Responding = True Then
        'kuanza = 1
        '
        ' Else
        ' Forces the process to close if the Responding value is False.
        ' kuanza = 1
        ' Timer1.Stop()
        'End If








    End Sub

   

    Private Sub txtResult_TextChanged(sender As System.Object, e As System.EventArgs)
        'lblTim.Text = kuanza'


    End Sub

    Private Sub btntest_Click(sender As System.Object, e As System.EventArgs)






    End Sub

    Private Sub Timer_Tick(sender As System.Object, e As System.EventArgs)

    End Sub

    Private Sub Timer_Tick_1(sender As System.Object, e As System.EventArgs)


    End Sub

    Private Sub FolderBrowserDialog1_HelpRequest(sender As System.Object, e As System.EventArgs)

    End Sub

    Private Sub Button1_Click_1(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level1.py")
    End Sub

    Private Sub Button2_Click(sender As System.Object, e As System.EventArgs) Handles Button2.Click
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level2.py")
    End Sub

    Private Sub Button3_Click(sender As System.Object, e As System.EventArgs) Handles Button3.Click
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level3.py")
    End Sub

    Private Sub Button4_Click(sender As System.Object, e As System.EventArgs) Handles Button4.Click
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level4.py")
    End Sub

    Private Sub Button5_Click(sender As System.Object, e As System.EventArgs) Handles Button5.Click
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level5.py")
    End Sub

    Private Sub Button6_Click(sender As System.Object, e As System.EventArgs) Handles Button6.Click
        Shell("C:\Python33\python.exe C:\Desktop\projects\game\level6.py")
    End Sub

    Private Sub Button7_Click(sender As System.Object, e As System.EventArgs)
        My.Computer.Audio.Stop()

    End Sub

    Private Sub Button7_Click_1(sender As System.Object, e As System.EventArgs) Handles Button7.Click
        My.Computer.Audio.Stop()

    End Sub
End Class
