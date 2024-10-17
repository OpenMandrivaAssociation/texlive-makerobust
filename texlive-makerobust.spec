Name:		texlive-makerobust
Version:	52811
Release:	2
Summary:	Making a macro robust (legacy package)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makerobust
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makerobust.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makerobust.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Heiko Oberdiek's makerobust package defined a command with name
\MakeRobustCommand that could be used to make fragile commands
robust. The LaTeX format has, since 2015, included a command
\MakeRobust with the same syntax and behaviour. Also by 2019,
almost all commands in LaTeX that may be used in a moving
argument are already robust. This package is now just a simple
one-liner defining the name \MakeRobustCommand as an alias for
\MakeRobust. This package should not be used in any new
documents.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/makerobust
%doc %{_texmfdistdir}/doc/latex/makerobust

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
