{
  description = "brain";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      inherit (nixpkgs.lib) genAttrs;
      systems = [ "x86_64-linux" ]; # "x86_64-darwin" "aarch64-linux" "aarch64-darwin"];
      forSystem =
        f: system:
        f (
          import nixpkgs {
            inherit system;
            # needed for science aspell dictionary
            config.allowUnfree = true;
          }
        );
      forAllSystems = f: genAttrs systems (forSystem f);
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            zk
            hugo
            nodePackages.pnpm
            (aspellWithDicts (
              ds: with ds; [
                en
                en-computers
                en-science
              ]
            ))
          ];
        };
      });
    };
}
