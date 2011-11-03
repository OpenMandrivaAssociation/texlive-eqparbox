# revision 16589
# category Package
# catalog-ctan /macros/latex/contrib/eqparbox
# catalog-date 2010-01-02 22:18:51 +0100
# catalog-license lppl
# catalog-version 3.1
Name:		texlive-eqparbox
Version:	3.1
Release:	1
Summary:	Create equal-widthed parboxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqparbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
LaTeX users sometimes need to ensure that two or more blocks of
text occupy the same amount of horizontal space on the page. To
that end, the eqparbox package defines a new command,
\eqparbox, which works just like \parbox, except that instead
of specifying a width, one specifies a tag. All eqparboxes with
the same tag--regardless of where they are in the document--
will stretch to fit the widest eqparbox with that tag. This
simple, equal-width mechanism can be used for a variety of
alignment purposes, as is evidenced by the examples in
eqparbox's documentation. Various derivatives of \eqparbox are
also provided.

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
%{_texmfdistdir}/tex/latex/eqparbox/eqparbox.sty
%doc %{_texmfdistdir}/doc/latex/eqparbox/README
%doc %{_texmfdistdir}/doc/latex/eqparbox/eqparbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eqparbox/eqparbox.dtx
%doc %{_texmfdistdir}/source/latex/eqparbox/eqparbox.ins
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
