VERSION 5.00
Begin VB.Form Main 
   Caption         =   "ÌÀÔ²Ë¢Êý¾Ý"
   ClientHeight    =   4245
   ClientLeft      =   225
   ClientTop       =   570
   ClientWidth     =   7440
   LinkTopic       =   "Form1"
   ScaleHeight     =   4245
   ScaleWidth      =   7440
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin VB.CommandButton Command5 
      Caption         =   "..."
      BeginProperty Font 
         Name            =   "ËÎÌå"
         Size            =   9
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   5280
      TabIndex        =   11
      Top             =   1080
      Width           =   495
   End
   Begin VB.CommandButton Command3 
      Caption         =   "Ë¢ÆÀÂÛ"
      Height          =   495
      Left            =   6000
      TabIndex        =   10
      Top             =   1440
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      Caption         =   "Ë¢ÔÄ¶Á"
      Height          =   495
      Left            =   6000
      TabIndex        =   9
      Top             =   0
      Width           =   1095
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Ë¢ÊÕ²Ø"
      Height          =   495
      Left            =   6000
      TabIndex        =   8
      Top             =   720
      Width           =   1095
   End
   Begin VB.TextBox Text2 
      Height          =   375
      Left            =   1200
      TabIndex        =   5
      Top             =   240
      Width           =   4575
   End
   Begin VB.TextBox Text4 
      Height          =   375
      Left            =   1200
      TabIndex        =   3
      Top             =   1920
      Width           =   4575
   End
   Begin VB.TextBox Text3 
      Height          =   375
      Left            =   1200
      TabIndex        =   2
      Top             =   1080
      Width           =   4095
   End
   Begin VB.CommandButton Command4 
      Caption         =   "Ë¢¹Ø×¢"
      Height          =   495
      Left            =   6000
      TabIndex        =   1
      Top             =   2160
      Width           =   1095
   End
   Begin VB.TextBox Text1 
      Height          =   855
      Left            =   120
      MultiLine       =   -1  'True
      ScrollBars      =   2  'Vertical
      TabIndex        =   0
      Top             =   3240
      Width           =   7215
   End
   Begin VB.Label Label4 
      Caption         =   "¹ºÂòÕËºÅ¼ÓQQ£º2223513246"
      BeginProperty Font 
         Name            =   "ËÎÌå"
         Size            =   15
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000FF&
      Height          =   495
      Left            =   1200
      TabIndex        =   12
      Top             =   2520
      Width           =   5175
   End
   Begin VB.Label Label3 
      Caption         =   "ÊýÁ¿£º"
      Height          =   255
      Left            =   480
      TabIndex        =   7
      Top             =   1920
      Width           =   975
   End
   Begin VB.Label Label2 
      Caption         =   "ÆÀÂÛ´Ê¿â£º"
      Height          =   255
      Left            =   120
      TabIndex        =   6
      Top             =   1200
      Width           =   975
   End
   Begin VB.Label Label1 
      Caption         =   "ÊéºÅ£º"
      Height          =   495
      Left            =   480
      TabIndex        =   4
      Top             =   360
      Width           =   855
   End
End
Attribute VB_Name = "Main"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Frame1_DragDrop(Source As Control, X As Single, Y As Single)

End Sub

Private Sub Label4_Click()

End Sub

Private Sub Menu_help_Click()

End Sub
