# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

a = Analysis(
    ['main.py'],
    pathex=['D:/OneDrive/Documents/university_lesson/Code_Projects/BillAssistant/src'],
    binaries=[],
    datas=[
        ('./main.kv', '.'),
        ('./ScreenOne/*', 'ScreenOne'),
        ('./ScreenThree/*', 'ScreenThree'),
        ('./ScreenTwo/*', 'ScreenTwo'),
        ('./WelcomeScreen/*', 'WelcomeScreen'),
        ('./apputils.py', '.'),
        ('./images/*', 'images')
    ],
    hiddenimports=['keyboard'],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='BillAssistant',
    icon='images/icon.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    options={"build_exe": {"dir": "dist"}},
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='dist\\BillAssistant')
