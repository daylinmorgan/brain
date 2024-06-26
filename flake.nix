{
  description = "brain";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      inherit (nixpkgs.lib) genAttrs;
      forAllSystems =
        f:
        genAttrs [ "x86_64-linux" ] # "x86_64-darwin" "aarch64-linux" "aarch64-darwin"]
          (system: f nixpkgs.legacyPackages.${system});
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          buildInputs = with pkgs; [
            zk
            hugo
            nodePackages.pnpm
          ];
        };
      });
    };
}
