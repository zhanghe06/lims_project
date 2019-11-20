# -*- mode: python ; coding: utf-8 -*-

# pip install pyinstaller
# pip install pywin32

# 初次创建
# pyinstaller -n lims -D run_apps.py  # 进入项目目录
# 生成 build、dist、lims.spec，build目录下lims即为工程包，exe在里面
# 修改 lims.spec，删除 build、dist
# pyinstaller lims.spec  # 重新打包

# 后续只需
# pyinstaller lims.spec


block_cipher = None


a = Analysis(['run_apps.py'],
             pathex=['%USERPROFILE%\\lims_project'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='lims',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='lims')
