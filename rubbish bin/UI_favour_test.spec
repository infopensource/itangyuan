# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\computer\\python³ÌÐò\\itangyuan\\UI_favour_test.py'],
             pathex=['D:\\computer\\python³ÌÐò\\itangyuan'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UI_favour_test',
          debug=False,
          strip=False,
          upx=True,
          console=False )
