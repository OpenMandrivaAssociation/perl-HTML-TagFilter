%define upstream_name HTML-TagFilter
%define upstream_version 1.03

Summary:	Fine-grained html-filter, xss-blocker and mailto-obfuscator
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/HTML-TagFilter/
Source:		http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Parser)
BuildArch:	noarch

%description
HTML::TagFilter is a subclass of HTML::Parser with a
single purpose: it will remove unwanted html tags and attributes from a
piece of text. It can act in a more or less fine-grained way - you can
specify permitted tags, permitted attributes of each tag, and permitted
values for each attribute in as much detail as you like.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/HTML/TagFilter.pm

%changelog
* Fri Sep 02 2011 Александр Казанцев <kazancas@mandriva.org> 1.03-1mdv2012.0
+ Revision: 697895
- imported package perl-HTML-TagFilter
- imported package perl-HTML-TagFilter


* Wed Jan 12 2011 Alexander Kazancev <kazancas@mandriva.ru> - 1.03-1
- Rebuild for Mandriva