'Poll Father v3
'2022-09-07

voteCount = 0
votes = 10

Set ie = createObject("InternetExplorer.Application")

Sub WaitForLoad
 Do While ie.Busy
  Wscript.Sleep 250
 Loop
End Sub

ie.left = 0
ie.top = 0
ie.toolbar = 0
ie.statusbar = 0
ie.height = 800
ie.width = 800
ie.resizable = 0

Call WaitForLoad

ie.navigate "https://www.dnj.com/story/sports/high-school/2022/09/04/vote-murfreesboro-area-high-school-girls-athlete-week/7906358001/" 'poll-specific

''''''''''''
Sub VoteForA
''''''''''''

Call WaitForLoad
ie.visible = 1

ie.Document.All.Item("PDI_answer51184562").Click 'poll-specific

ie.Document.All.Item("pd-vote-button11192890").Click 'poll-specific

Call WaitForLoad

ie.navigate "https://www.dnj.com/story/sports/high-school/2022/09/04/vote-murfreesboro-area-high-school-girls-athlete-week/7906358001/" 'poll-specific

'''''''
End Sub
'''''''

Do While voteCount < votes
 Call VoteForA
Loop

ie.quit
wscript.quit