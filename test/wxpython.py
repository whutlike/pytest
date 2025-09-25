import wx

# 创建应用程序对象
app = wx.App()

# 创建窗口
frm = wx.Frame(None, title='初中化学', size=(600, 800), pos=(100, 100))
# 显示窗口
# frm.Show()

# 创建面板，创建在frm上
pnl = wx.Panel(frm)
# 显示面板
# pnl.Show()

# 创建静态文本
st = wx.StaticText(pnl, label='初中化学', pos=(0, 0))
# 显示静态文本
# st.Show()

# 创建按钮
btn = wx.Button(pnl, label='开始', pos=(0, 50))
# 显示按钮

frm.Show()
# 进入主循环，让窗口一直显示
app.MainLoop()