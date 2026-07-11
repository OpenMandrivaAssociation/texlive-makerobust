%global tl_name makerobust
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Making a macro robust (legacy package)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makerobust
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makerobust.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makerobust.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Heiko Oberdiek's makerobust package defined a command with name
\MakeRobustCommand that could be used to make fragile commands robust.
The LaTeX format has, since 2015, included a command \MakeRobust with
the same syntax and behaviour. Also by 2019, almost all commands in
LaTeX that may be used in a moving argument are already robust. This
package is now just a simple one-liner defining the name
\MakeRobustCommand as an alias for \MakeRobust. This package should not
be used in any new documents.

