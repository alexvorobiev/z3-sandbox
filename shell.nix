{ pkgs ? import <nixpkgs> {} }:
with pkgs;
mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = [
    (python3.withPackages (ps: with python3Packages; [ z3 ipython python-lsp-server ]))
  ];
}
