%global tl_name eqparbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1
Release:	%{tl_revision}.1
Summary:	Create equal-widthed parboxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqparbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqparbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX users sometimes need to ensure that two or more blocks of text
occupy the same amount of horizontal space on the page. To that end, the
eqparbox package defines a new command, \eqparbox, which works just like
\parbox, except that instead of specifying a width, one specifies a tag.
All eqparboxes with the same tag--regardless of where they are in the
document--will stretch to fit the widest eqparbox with that tag. This
simple, equal-width mechanism can be used for a variety of alignment
purposes, as is evidenced by the examples in eqparbox's documentation.
Various derivatives of \eqparbox are also provided.

