Name:		texlive-dprogress
Version:	15878
Release:	2
Summary:	LaTeX-relevant log information for debugging
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dprogress
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package logs LaTeX's progress through the file, making the
LaTeX output more verbose. This helps to make LaTeX debugging
easier, as it is simpler to find where exactly LaTeX failed.
The package outputs the typesetting of section, subsection and
subsubsection headers and (if amsmath is loaded) details of the
align environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dprogress/dprogress.sty
%doc %{_texmfdistdir}/doc/latex/dprogress/README
%doc %{_texmfdistdir}/doc/latex/dprogress/dprogress.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dprogress/dprogress.dtx
%doc %{_texmfdistdir}/source/latex/dprogress/dprogress.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
