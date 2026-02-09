{
  description = "CustomTkinter Flake - Niri/Wayland Fix";

  inputs = {
    nixpkgs.url = "github:Nixos/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          customtkinter
          tkinter 
        ]);
        
        runtimeLibs = with pkgs; [
          xorg.libX11
          xorg.libXcursor
          xorg.libXext
          xorg.libXrender
          xorg.libXft
          libGL
          libxkbcommon
          fontconfig
          wayland
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            pkgs.tk
            pkgs.tcl
            pkgs.xwayland
            pkgs.xorg.xhost
            pkgs.xorg.xauth
          ] ++ runtimeLibs;

          shellHook = ''
            export TK_LIBRARY="${pkgs.tk}/lib/tk8.6"
            export TCL_LIBRARY="${pkgs.tcl}/lib/tcl8.6"
            export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath runtimeLibs}:$LD_LIBRARY_PATH"
            
            # Niri/Wayland specific: 
            # If DISPLAY isn't set, try to find the XWayland socket
            if [ -z "$DISPLAY" ]; then
              export DISPLAY=$(ls /tmp/.X11-unix/X* | head -n 1 | sed 's|.*X|:|')
            fi

            # Ensure the Xauthority is pointed to your home session
            export XAUTHORITY=$HOME/.Xauthority

            echo "🚀 Niri GUI Environment Loaded (Display: $DISPLAY)"
            
            # Fix font permissions automatically
            mkdir -p $HOME/.fonts
            
            # Try to relax X11 permissions for the local user
            xhost +local:$(whoami) > /dev/null 2>&1 || echo "Note: xhost could not set permissions."
          '';
        };
      });
}
