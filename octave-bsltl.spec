%global octpkg bsltl

Summary:	Functions for working with the biospeckle laser technique in Octave
Name:		octave-bsltl
Version:	1.3.1
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/bsltl/
Source0:	https://downloads.sourceforge.net/octave/bsltl-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Free collection of Octave/MATLAB routines for working with the
biospeckle laser technique.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

