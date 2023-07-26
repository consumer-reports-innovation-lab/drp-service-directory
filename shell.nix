{ pkgs ? import <nixpkgs> {} }:

with pkgs;
let
  myPython = python3.withPackages( pp: with pp; [
    jsonschema
  ]);
in mkShell {
  packages= [
    myPython

    isort
    black
  ];
}
