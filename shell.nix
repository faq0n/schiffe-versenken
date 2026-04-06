with import <nixpkgs> { };
let
  pythonEnv = python313.withPackages (ps: [
    ps.requests
    ps.toolz
  ]);
in
mkShell {
  packages = [
    pythonEnv

    black
    mypy
  ];
}
