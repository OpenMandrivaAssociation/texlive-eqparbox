# revision 16589
# category Package
# catalog-ctan /macros/latex/contrib/eqparbox
# catalog-date 2010-01-02 22:18:51 +0100
# catalog-license lppl
# catalog-version 3.1
Name:		texlive-eqparbox
Version:	3.1
Release:	2
Summary:	Create equal-widthed parboxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqparbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqparbox/eqparbox.sty
%doc %{_texmfdistdir}/doc/latex/eqparbox/README
%doc %{_texmfdistdir}/doc/latex/eqparbox/eqparbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eqparbox/eqparbox.dtx
%doc %{_texmfdistdir}/source/latex/eqparbox/eqparbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-2
+ Revision: 751540
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1-1
+ Revision: 718359
- texlive-eqparbox
- texlive-eqparbox
- texlive-eqparbox
- texlive-eqparbox

