%define		addon	autogrow
Summary:	AutoGrow plugin
Name:		ckeditor-addon-%{addon}
Version:	4.2.3
Release:	1
# License: same as ckeditor
License:	LGPL v2.1+ / GPL v2+ / MPL
Group:		Applications/WWW
Source0:	http://download.ckeditor.com/autogrow/releases/autogrow_%{version}.zip
# Source0-md5:	47d9ff305241de389e60c0c73de27d13
URL:		http://ckeditor.com/addon/autogrow
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	ckeditor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/ckeditor
%define		_pluginsdir	%{_appdir}/plugins

%description
With this plugin, the editor content space will automatically expand
horizontally to fit the content.

The following configuration options are available:
- maximum and minimum autogrow size.
- have autogrow happen on editor startup

Note: This plugin is to be used with the themedui creato

%prep
%setup -qc
mv %{addon}/samples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pluginsdir}
cp -a %{addon} $RPM_BUILD_ROOT%{_pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc samples
%{_pluginsdir}/%{addon}
