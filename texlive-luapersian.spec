# revision 23576
# category Package
# catalog-ctan /macros/luatex/latex/luapersian
# catalog-date 2011-07-18 09:05:38 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-luapersian
Version:	0.1
Release:	4
Summary:	Persian for LaTeX in LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luapersian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapersian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luapersian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Persian for LaTeX in LuaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luapersian/algorithm-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/algorithmic-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/amsart-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/amsbook-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/amsmath-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/amstext-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/array-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/article-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/artikel1-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/artikel2-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/artikel3-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/arydshln-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/backref-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/boek-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/boek3-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/book-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/bookest-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/breqn-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/color-localise-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/commands-ltx-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/commands-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/enumerate-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/environments-ltx-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/environments-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/extarticle-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/extbook-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/extletter-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/extreport-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/fancyhdr-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/fleqn-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/flowfram-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/hvfloat-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/hyperref-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/leqno-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/letter-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/listings-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/loadingorder-luapersian.sty
%{_texmfdistdir}/tex/lualatex/luapersian/localise-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/luapersian-footnote.sty
%{_texmfdistdir}/tex/lualatex/luapersian/luapersian-mathsdigitspec.sty
%{_texmfdistdir}/tex/lualatex/luapersian/luapersian-multiplechoice.sty
%{_texmfdistdir}/tex/lualatex/luapersian/luapersian-persiancal.sty
%{_texmfdistdir}/tex/lualatex/luapersian/luapersian.sty
%{_texmfdistdir}/tex/lualatex/luapersian/luapersianftnxtra.sty
%{_texmfdistdir}/tex/lualatex/luapersian/memoir-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/messages-localise-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/minitoc-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/misc-localise-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/natbib-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/packages-localise-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/pgf-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/ragged2e-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/rapport1-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/rapport3-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/refrep-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/report-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/scrartcl-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/scrbook-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/scrreprt-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/sidecap-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/stabular-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/tabls-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/tabulary-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/tikz-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/tocbibind-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/tocloft-luapersian.def
%{_texmfdistdir}/tex/lualatex/luapersian/wrapfig-luapersian.def
%doc %{_texmfdistdir}/doc/lualatex/luapersian/README
%doc %{_texmfdistdir}/doc/lualatex/luapersian/luapersian.ltx
%doc %{_texmfdistdir}/doc/lualatex/luapersian/luapersian.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 753589
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 718928
- texlive-luapersian
- texlive-luapersian
- texlive-luapersian
- texlive-luapersian

