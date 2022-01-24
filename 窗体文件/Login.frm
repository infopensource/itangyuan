VERSION 5.00
Begin VB.Form Login 
   BackColor       =   &H0000FF00&
   Caption         =   "登录"
   ClientHeight    =   1410
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4545
   FillColor       =   &H0000FF00&
   ForeColor       =   &H0000FF00&
   LinkTopic       =   "Form1"
   ScaleHeight     =   1410
   ScaleWidth      =   4545
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command1 
      BackColor       =   &H0000FF00&
      Caption         =   "注册"
      Height          =   975
      Left            =   3720
      TabIndex        =   4
      Top             =   240
      Width           =   615
   End
   Begin VB.TextBox Text2 
      Height          =   375
      Left            =   840
      TabIndex        =   3
      Top             =   840
      Width           =   2655
   End
   Begin VB.TextBox Text1 
      Height          =   375
      Left            =   840
      TabIndex        =   1
      Top             =   240
      Width           =   2655
   End
   Begin VB.Label Label2 
      BackColor       =   &H0000FF00&
      Caption         =   "密码"
      Height          =   255
      Left            =   120
      TabIndex        =   2
      Top             =   840
      Width           =   1215
   End
   Begin VB.Label Label1 
      BackColor       =   &H0000FF00&
      Caption         =   "用户名"
      Height          =   255
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   1215
   End
End
Attribute VB_Name = "Login"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
MsgBox "1"
End Sub
