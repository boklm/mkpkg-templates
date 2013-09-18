[%-
  SET rel = 1;
  IF p.describe.tag_reach;
        rel = '0.' _ p.describe.tag_reach _ '.g' _ p.describe.hash;
  END;
-%]
Name:           [% project %]
Version:        [% c('version') %]
Release:        [% d.rel_macro %] [% rel %]
Source:         %{name}-%{version}.tar.[% c('compress_tar') %]
Summary:        [% p.summary %]
URL:            [% p.url %]
License:        CC0
Group:          Text tools
BuildArch:      noarch
%description
[% p.description -%]

%prep
%setup -q

%build

%install
%makeinstall_std perldir=%{perl_vendorlib}

%files
%doc README.md COPYING
%{_bindir}/%{name}
%{perl_vendorlib}/MkPkg.pm
