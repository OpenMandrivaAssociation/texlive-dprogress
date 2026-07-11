%global tl_name dprogress
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	LaTeX-relevant log information for debugging
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dprogress
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package logs LaTeX's progress through the file, making the LaTeX
output more verbose. This helps to make LaTeX debugging easier, as it is
simpler to find where exactly LaTeX failed. The package outputs the
typesetting of section, subsection and subsubsection headers and (if
amsmath is loaded) details of the align environment.

