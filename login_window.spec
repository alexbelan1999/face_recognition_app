# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['windows\\login_window.py'],
             pathex=['C:\\Users\\Alex\\PycharmProjects\\face_recognition_app'],
             binaries=[],
             datas = [('C:\\Users\\Alex\\PycharmProjects\\face_recognition_app\\venv\\Lib\\site-packages\\face_recognition_models','face_recognition_models'),
             ('python_icon.ico','python_icon.ico')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='login_window',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='python_icon.ico')
