# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['windows/login_window.py'],
             pathex=['/home/alex/PycharmProjects/face_recognition_app'],
             binaries=[],
             datas = [
             ('/home/alex/PycharmProjects/face_recognition_app/venv/lib/python3.7/site-packages/face_recognition_models','face_recognition_models'),
             ('/home/alex/PycharmProjects/face_recognition_app/venv/lib/python3.7/site-packages/face_recognition','face_recognition'),
             ('icon/python_icon.ico','icon')
             ],
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
          name='face_rec_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='python_icon.ico')