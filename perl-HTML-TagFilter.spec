%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TagFilter

Summary: Fine-grained html-filter, xss-blocker and mailto-obfuscator
Name: perl-HTML-TagFilter
Version: 1.03
Release: %mkrel 1
License: Artistic/GPL
Group: Development/Perl
URL: http://search.cpan.org/dist/HTML-TagFilter/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-TagFilter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
HTML::TagFilter is a subclass of HTML::Parser with a
single purpose: it will remove unwanted html tags and attributes from a
piece of text. It can act in a more or less fine-grained way - you can
specify permitted tags, permitted attributes of each tag, and permitted
values for each attribute in as much detail as you like.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/TagFilter.pm

