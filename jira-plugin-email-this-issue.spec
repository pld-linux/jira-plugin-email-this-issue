%define		plugin	email-this-issue
Summary:	JIRA "Email this issue" plugin
Name:		jira-plugin-%{plugin}
Version:	1.8
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries/Java
Source0:	https://studio.plugins.atlassian.com/wiki/download/attachments/2261441/email-this-issue-plugin-%{version}.jar
# Source0-md5:	9290b62d79d257c58b5661b74dbbc4b0
URL:		https://plugins.atlassian.com/plugin/details/4977
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jira >= 4.1.1-2
Obsoletes:	jira-enterprise-plugin-email-this-issue
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_datadir}/jira/plugins
%define		pluginsdeploydir	%{_datadir}/jira/WEB-INF/lib

%description
This plugin contains an issue operation component that allows users to
compose an email and send the issue to arbitrary recipients.

Most important features are:

- send email with issue details to email addresses outside JIRA,
  assignee, reporter and watchers.
- attach issue attachments to email
- control who can invoke the operation through a project role
- text and html email format are supported, email body understands
  Confluence wiki markup
- email template can be customized per project and issue type
- a comment is created reflecting the event of sending an email (body,
  recipients, etc) - see below
- i18n-enabled, the plugin can be translated, it is currently
  available in English, German, French, Polish and Hungarian.
- you have options like "CC to me" and "Reply to me" to receive a copy
  of the email or to receive replies to the email.
- email recipients are added to watchers on demand
- recipients from custom fields and groups/project roles can be added
- email options may be reused, i.e. there is no need to check all your
  options every time you send an email

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{pluginsdeploydir},%{pluginsdir}}
cp %{SOURCE0} $RPM_BUILD_ROOT%{pluginsdir}/plugin-%{plugin}-%{version}.jar
ln -s %{pluginsdir}/plugin-%{plugin}-%{version}.jar $RPM_BUILD_ROOT%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{pluginsdir}/plugin-%{plugin}-%{version}.jar
%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar
