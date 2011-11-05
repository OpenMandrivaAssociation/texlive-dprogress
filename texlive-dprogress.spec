# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dprogress
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-dprogress
Version:	0.1
Release:	1
Summary:	LaTeX-relevant log information for debugging
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dprogress
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dprogress.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package logs LaTeX's progress through the file, making the
LaTeX output more verbose. This helps to make LaTeX debugging
easier, as it is simpler to find where exactly LaTeX failed.
The package outputs the typesetting of section, subsection and
subsubsection headers and (if amsmath is loaded) details of the
align environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dprogress/dprogress.sty
%doc %{_texmfdistdir}/doc/latex/dprogress/README
%doc %{_texmfdistdir}/doc/latex/dprogress/dprogress.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dprogress/dprogress.dtx
%doc %{_texmfdistdir}/source/latex/dprogress/dprogress.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
