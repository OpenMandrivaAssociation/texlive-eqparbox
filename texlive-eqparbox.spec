Name:		texlive-eqparbox
Version:	45215
Release:	2
Summary:	Create equal-widthed parboxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqparbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
