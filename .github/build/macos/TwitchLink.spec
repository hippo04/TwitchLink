APP_NAME = "TwitchLink"
APP_DISPLAYNAME = "TwitchLink"
APP_VERSION = "{{APP_VERSION}}"
APP_IDENTIFIER = "io.github.twitchlink"
APP_HOMEPAGE = "https://twitchlink.github.io"


a = Analysis(
    ["TwitchLink.py"],
    pathex=[],
    binaries=[],
    datas=[("resources", "resources")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=["resources/icons/icon.icns"],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME,
)

app = BUNDLE(
    coll,
    name=f"{APP_NAME}.app",
    icon="resources/icons/icon.icns",
    bundle_identifier=APP_IDENTIFIER,
    version=APP_VERSION,
    info_plist={
        "CFBundleName": APP_NAME,
        "CFBundleDisplayName": APP_DISPLAYNAME,
        "CFBundleIdentifier": APP_IDENTIFIER,
        "CFBundleVersion": APP_VERSION,
        "CFBundleShortVersionString": APP_VERSION,
        "NSPrincipalClass": "NSApplication",
        "CFBundlePackageType": "APPL",
        "NSHighResolutionCapable": True,
        "CFBundleIconFile": "icon.icns",
        "CFBundleHomepage": APP_HOMEPAGE
    }
)
