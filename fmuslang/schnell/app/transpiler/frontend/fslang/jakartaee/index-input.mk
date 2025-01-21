--% index/fmus
fs-jee,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.gitignore)
	docker-compose.yml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/docker-compose.yml)
	Dockerfile,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/Dockerfile)
	LICENSE,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/LICENSE)
	pom.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/pom.xml)
	README.md,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/README.md)
	run.sh,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/run.sh)
	.github,d(/mk)
		dependabot.yml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/dependabot.yml)
		ISSUE_TEMPLATE,d(/mk)
			bug_report.md,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/ISSUE_TEMPLATE/bug_report.md)
		workflows,d(/mk)
			it-with-arq-payara-managed.yml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/workflows/it-with-arq-payara-managed.yml)
			maven.yml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/workflows/maven.yml)
	src,d(/mk)
		main,d(/mk)
			java,d(/mk)
				com,d(/mk)
					example,d(/mk)
						application,d(/mk)
							util,d(/mk)
								LoggerProducer.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/LoggerProducer.java)
								SampleDataPopulator.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/SampleDataPopulator.java)
								hash,d(/mk)
									Crypto.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/Crypto.java)
									PasswordEncoder.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/PasswordEncoder.java)
									PasswordEncoderProducer.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/PasswordEncoderProducer.java)
									bcrypt,d(/mk)
										BCrypt.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/BCrypt.java)
										BCryptPasswordEncoder.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/BCryptPasswordEncoder.java)
										package-info.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/package-info.java)
									plain,d(/mk)
										PlainPasswordEncoder.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/plain/PlainPasswordEncoder.java)
						domain,d(/mk)
							common,d(/mk)
								AbstractAuditableEntity.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AbstractAuditableEntity.java)
								AbstractEntity.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AbstractEntity.java)
								AuditingEntityListener.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AuditingEntityListener.java)
								Boolean2StringConverter.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/Boolean2StringConverter.java)
								Username.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/Username.java)
							task,d(/mk)
								Count.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Count.java)
								Existence.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Existence.java)
								Task.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Task.java)
								TaskRepository.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/TaskRepository.java)
							user,d(/mk)
								User.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/user/User.java)
								UserRepository.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/user/UserRepository.java)
						infrastructure,d(/mk)
							package-info.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/package-info.java)
							persistence,d(/mk)
								jpa,d(/mk)
									AbstractRepository.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/AbstractRepository.java)
									JpaTaskRepository.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/JpaTaskRepository.java)
									JpaUserRepository.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/JpaUserRepository.java)
							security,d(/mk)
								Authenticated.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/Authenticated.java)
								AuthenticatedUserInfoProducer.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/AuthenticatedUserInfoProducer.java)
								SecurityConstant.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/SecurityConstant.java)
								UserInfo.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/UserInfo.java)
								jwt,d(/mk)
									JpaIdentityStore.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JpaIdentityStore.java)
									JwtAuthenticationMechanism.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtAuthenticationMechanism.java)
									JwtCredential.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtCredential.java)
									JwtProperties.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtProperties.java)
									JwtRememberMeIdentityStore.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtRememberMeIdentityStore.java)
									package-info.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/package-info.java)
									TokenProvider.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/TokenProvider.java)
						interfaces,d(/mk)
							RestConfiguration.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/RestConfiguration.java)
							auth,d(/mk)
								AuthResource.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/auth/AuthResource.java)
							common,d(/mk)
								PagedResult.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PagedResult.java)
								PageParam.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PageParam.java)
								PrimitiveConverterProvider.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PrimitiveConverterProvider.java)
								cors,d(/mk)
									CorsFeature.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsFeature.java)
									CorsFilter.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsFilter.java)
									CorsHeaders.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsHeaders.java)
									package-info.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/package-info.java)
								exceptionMapper,d(/mk)
									ConstraintViolationExceptionMapper.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/exceptionMapper/ConstraintViolationExceptionMapper.java)
							profile,d(/mk)
								CurrentUserResource.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/profile/CurrentUserResource.java)
							task,d(/mk)
								TaskForm.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskForm.java)
								TaskNotFoundException.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskNotFoundException.java)
								TaskNotFoundExceptionMapper.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskNotFoundExceptionMapper.java)
								TaskResource.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskResource.java)
								TaskResources.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskResources.java)
								UpdateStatusRequest.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/UpdateStatusRequest.java)
							user,d(/mk)
								EmailWasTakenException.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/EmailWasTakenException.java)
								EmailWasTakenExceptionMapper.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/EmailWasTakenExceptionMapper.java)
								RegisterForm.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/RegisterForm.java)
								UserForm.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserForm.java)
								UserMessageBodyWiter.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserMessageBodyWiter.java)
								UsernameWasTakenException.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsernameWasTakenException.java)
								UsernameWasTakenExceptionMapper.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsernameWasTakenExceptionMapper.java)
								UserResource.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserResource.java)
								UsersResource.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsersResource.java)
			liberty,d(/mk)
				config,d(/mk)
					server.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/liberty/config/server.xml)
			resources,d(/mk)
				META-INF,d(/mk)
					microprofile-config.properties,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/microprofile-config.properties)
					orm.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/orm.xml)
					persistence.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/persistence.xml)
			webapp,d(/mk)
				WEB-INF,d(/mk)
					beans.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/beans.xml)
					glassfish-web.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/glassfish-web.xml)
					web.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/web.xml)
		test,d(/mk)
			java,d(/mk)
				com,d(/mk)
					example,d(/mk)
						.gitkeep,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/.gitkeep)
						it,d(/mk)
							TaskRepositoryTest.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/it/TaskRepositoryTest.java)
							TaskResourceTest.java,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/it/TaskResourceTest.java)
			resources,d(/mk)
				arquillian.xml,f(e=utama=/tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/resources/arquillian.xml)
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.gitignore
/target/
/.idea
*.iml

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/docker-compose.yml
version: '3'
services:
  jboss:
    build: .
    ports:
      - "8080:8080"
      - "9990:9990"
    # restart: always
    command: /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/Dockerfile
FROM jboss/wildfly:17.0.1.Final
# COPY build/libs/jakarta-ee-getting-started.war /opt/jboss/wildfly/standalone/deployments/
COPY target/jakartaee-jaxrs-sample.war /opt/jboss/wildfly/standalone/deployments/

# FROM jboss/wildfly
# ADD ./target/jakartaee-jaxrs-sample.war /opt/jboss/wildfly/standalone/deployments/
# RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin#70365 --silent

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {one line to give the program's name and a brief idea of what it does.}
    Copyright (C) {year}  {name of author}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>jakartaee-jaxrs-sample</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>
    <name>jakartaee-jaxrs-sample</name>
    <description>A Jakarta EE MVC sample project</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <!-- since 3.0 it is set by default -->
        <!--<failOnMissingWebXml>false</failOnMissingWebXml>-->

        <!-- use Java 11 as default -->
        <maven.compiler.release>11</maven.compiler.release>

        <!-- Jakarta EE API -->
        <jakartaee-api.version>8.0.0</jakartaee-api.version>
        <microprofile.version>4.1</microprofile.version>
        <jjwt.version>0.11.2</jjwt.version>

        <!-- Maven Plugins -->
        <maven-compiler-plugin.version>3.8.1</maven-compiler-plugin.version>
        <maven-war-plugin.version>3.3.2</maven-war-plugin.version>
        <cargo-maven2-plugin.version>1.8.5</cargo-maven2-plugin.version>
        <maven-dependency-plugin.version>3.2.0</maven-dependency-plugin.version>
        <maven-surefire-plugin.version>3.0.0-M5</maven-surefire-plugin.version>
        <maven-failsafe-plugin.version>3.0.0-M5</maven-failsafe-plugin.version>
        <maven-surefire-report-plugin.version>3.0.0-M5</maven-surefire-report-plugin.version>

        <!-- Arquillian BOM -->
        <arquillian-bom.version>1.6.0.Final</arquillian-bom.version>

        <!-- Glassfish server -->
        <glassfish.version>5.1.0</glassfish.version>
        <arquillian-glassfish.version>1.0.2</arquillian-glassfish.version>
        <jersey.version>2.28</jersey.version>
        <eclipselink.version>2.7.10</eclipselink.version>

        <!-- Payara server -->
        <payara.version>5.2021.10</payara.version>
        <arquillian-payara.version>2.4.5</arquillian-payara.version>

        <!-- Wildfly server-->
        <wildfly.version>21.0.1.Final</wildfly.version>
        <wildfly-maven-plugin.version>2.1.0.Final</wildfly-maven-plugin.version>
        <wildfly-arquillian.version>2.2.0.Final</wildfly-arquillian.version>
        <!--  websockets-jsr and resteasy for client, aligned with Wildfly version. -->
        <undertow-websockets-jsr.version>2.0.26.Final</undertow-websockets-jsr.version>
        <resteasy.version>3.9.0.Final</resteasy.version>

        <!-- OpenLiberty server -->
        <liberty.runtime.version>20.0.0.12</liberty.runtime.version>
        <!-- WARNING: 10.15.x.x does not work with openliberty 20.0.0.1 -->
        <derby.version>10.14.2.0</derby.version>
        <liberty-maven-plugin.version>3.5.1</liberty-maven-plugin.version>

        <!-- By default, skip tests -->
        <skipTests>true</skipTests>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>jakarta.platform</groupId>
                <artifactId>jakarta.jakartaee-api</artifactId>
                <version>${jakartaee-api.version}</version>
                <scope>provided</scope>
            </dependency>
            <dependency>
                <groupId>org.eclipse.microprofile</groupId>
                <artifactId>microprofile</artifactId>
                <version>${microprofile.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.jboss.arquillian</groupId>
                <artifactId>arquillian-bom</artifactId>
                <version>${arquillian-bom.version}</version>
                <scope>import</scope>
                <type>pom</type>
            </dependency>

            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.13.2</version>
                <scope>test</scope>
            </dependency>
            <!-- https://mvnrepository.com/artifact/org.hamcrest/hamcrest -->
            <dependency>
                <groupId>org.hamcrest</groupId>
                <artifactId>hamcrest</artifactId>
                <version>2.2</version>
                <scope>test</scope>
            </dependency>

            <dependency>
                <groupId>org.skyscreamer</groupId>
                <artifactId>jsonassert</artifactId>
                <version>1.5.0</version>
                <scope>test</scope>
            </dependency>
            <!-- https://mvnrepository.com/artifact/org.awaitility/awaitility -->
            <dependency>
                <groupId>org.awaitility</groupId>
                <artifactId>awaitility</artifactId>
                <version>4.1.1</version>
                <scope>test</scope>
            </dependency>

            <!-- JSON path -->
            <dependency>
                <groupId>com.jayway.jsonpath</groupId>
                <artifactId>json-path</artifactId>
                <version>2.6.0</version>
                <scope>test</scope>
            </dependency>
            <!-- https://mvnrepository.com/artifact/com.jayway.jsonpath/json-path-assert -->
            <dependency>
                <groupId>com.jayway.jsonpath</groupId>
                <artifactId>json-path-assert</artifactId>
                <version>2.6.0</version>
                <scope>test</scope>
            </dependency>

            <!-- Mockito -->
            <!-- https://mvnrepository.com/artifact/org.mockito/mockito-core -->
            <dependency>
                <groupId>org.mockito</groupId>
                <artifactId>mockito-core</artifactId>
                <version>4.2.0</version>
                <scope>test</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>jakarta.platform</groupId>
            <artifactId>jakarta.jakartaee-api</artifactId>
        </dependency>
        <dependency>
            <groupId>org.eclipse.microprofile.config</groupId>
            <artifactId>microprofile-config-api</artifactId>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.22</version>
            <optional>true</optional>
        </dependency>

        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-api</artifactId>
            <version>${jjwt.version}</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-impl</artifactId>
            <version>${jjwt.version}</version>
            <scope>runtime</scope>
        </dependency>
        <!-- or jjwt-gson if Gson is preferred -->
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-jackson</artifactId>
            <version>${jjwt.version}</version>
            <scope>runtime</scope>
        </dependency>

        <dependency>
            <groupId>org.eclipse.persistence</groupId>
            <artifactId>org.eclipse.persistence.jpa.modelgen.processor</artifactId>
            <version>${eclipselink.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.jboss.arquillian.junit</groupId>
            <artifactId>arquillian-junit-container</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
        </dependency>
        <dependency>
            <groupId>org.hamcrest</groupId>
            <artifactId>hamcrest</artifactId>
        </dependency>
        <dependency>
            <groupId>org.awaitility</groupId>
            <artifactId>awaitility</artifactId>
        </dependency>
        <dependency>
            <groupId>org.skyscreamer</groupId>
            <artifactId>jsonassert</artifactId>
        </dependency>
        <!--        <dependency>
            <groupId>com.jayway.jsonpath</groupId>
            <artifactId>json-path</artifactId>
        </dependency>
        <dependency>
            <groupId>com.jayway.jsonpath</groupId>
            <artifactId>json-path-assert</artifactId>
        </dependency>     -->
    </dependencies>
    <build>
        <finalName>${project.artifactId}</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${maven-compiler-plugin.version}</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>${maven-war-plugin.version}</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${maven-surefire-plugin.version}</version>
                <configuration>
                    <skipTests>${skipTests}</skipTests>
                </configuration>
                <executions>
                    <execution>
                        <phase>test</phase>
                        <id>default-test</id>
                        <configuration>
                            <excludes>
                                <exclude>**/it/**</exclude>
                            </excludes>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-failsafe-plugin</artifactId>
                <version>${maven-failsafe-plugin.version}</version>
                <configuration>
                    <skipITs>${skipTests}</skipITs>
                </configuration>
                <executions>
                    <execution>
                        <phase>integration-test</phase>
                        <id>integration-test</id>
                        <goals>
                            <goal>integration-test</goal>
                            <goal>verify</goal>
                        </goals>
                        <configuration>
                            <includes>
                                <include>**/it/**</include>
                            </includes>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <profiles>
        <profile>
            <id>wildfly</id>
            <build>
                <plugins>
                    <!-- The WildFly plugin deploys your war to a local WildFly container -->
                    <!-- To use, run: mvn package wildfly:deploy -->
                    <plugin>
                        <groupId>org.wildfly.plugins</groupId>
                        <artifactId>wildfly-maven-plugin</artifactId>
                        <version>${wildfly-maven-plugin.version}</version>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>openliberty</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-dependency-plugin</artifactId>
                        <version>${maven-dependency-plugin.version}</version>
                        <executions>
                            <execution>
                                <id>copy</id>
                                <phase>package</phase>
                                <goals>
                                    <goal>copy</goal>
                                </goals>
                            </execution>
                        </executions>
                        <configuration>
                            <artifactItems>
                                <artifactItem>
                                    <groupId>org.apache.derby</groupId>
                                    <artifactId>derby</artifactId>
                                    <version>${derby.version}</version>
                                    <type>jar</type>
                                    <overWrite>false</overWrite>
                                </artifactItem>
                            </artifactItems>
                            <outputDirectory>${project.build.directory}/liberty/wlp/usr/shared/resources
                            </outputDirectory>
                        </configuration>
                    </plugin>
                    <!-- Enable liberty-maven-plugin -->
                    <plugin>
                        <groupId>io.openliberty.tools</groupId>
                        <artifactId>liberty-maven-plugin</artifactId>
                        <version>${liberty-maven-plugin.version}</version>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>payara-local</id>
            <properties>
                <glassfish.home>${project.build.directory}/payara5</glassfish.home>
                <glassfish.domainDir>${glassfish.home}/glassfish/domains</glassfish.domainDir>
                <glassfish.domainName>domain1</glassfish.domainName>
            </properties>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-dependency-plugin</artifactId>
                        <version>${maven-dependency-plugin.version}</version>
                        <executions>
                            <execution>
                                <id>unpack</id>
                                <phase>process-resources</phase>
                                <goals>
                                    <goal>unpack</goal>
                                </goals>
                                <configuration>
                                    <artifactItems>
                                        <artifactItem>
                                            <groupId>fish.payara.distributions</groupId>
                                            <artifactId>payara</artifactId>
                                            <version>${payara.version}</version>
                                            <type>zip</type>
                                            <outputDirectory>${project.build.directory}</outputDirectory>
                                        </artifactItem>
                                    </artifactItems>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                    <plugin>
                        <groupId>org.codehaus.cargo</groupId>
                        <artifactId>cargo-maven2-plugin</artifactId>
                        <version>${cargo-maven2-plugin.version}</version>
                        <configuration>
                            <container>
                                <containerId>payara</containerId>
                                <type>installed</type>
                                <home>${glassfish.home}</home>
                            </container>
                            <configuration>
                                <type>existing</type>
                                <home>${glassfish.domainDir}</home>
                                <properties>
                                    <cargo.glassfish.domain.name>${glassfish.domainName}</cargo.glassfish.domain.name>
                                    <cargo.remote.timeout>300000</cargo.remote.timeout>
                                    <cargo.remote.password></cargo.remote.password>
                                    <!-- add extra datasource :
                                    https://codehaus-cargo.github.io/cargo/DataSource+and+Resource+Support.html
                                    -->
                                    <!--<cargo.datasource.datasource.derby>
                                        cargo.datasource.driver=org.apache.derby.jdbc.EmbeddedDriver|
                                        cargo.datasource.url=jdbc:derby:derbyDB;create=true|
                                        cargo.datasource.jndi=jdbc/__default|
                                        cargo.datasource.transactionsupport=LOCAL_TRANSACTION|
                                        cargo.datasource.username=APP|
                                        cargo.datasource.password=nonemptypassword
                                    </cargo.datasource.datasource.derby>-->
                                </properties>
                            </configuration>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>payara-remote</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.codehaus.cargo</groupId>
                        <artifactId>cargo-maven2-plugin</artifactId>
                        <version>${cargo-maven2-plugin.version}</version>
                        <configuration>
                            <container>
                                <containerId>payara</containerId>
                                <type>remote</type>
                            </container>
                            <configuration>
                                <type>runtime</type>
                                <properties>
                                    <cargo.remote.username>admin</cargo.remote.username>
                                    <cargo.remote.password></cargo.remote.password>
                                    <cargo.glassfish.admin.port>4848</cargo.glassfish.admin.port>
                                    <cargo.hostname>localhost</cargo.hostname>
                                </properties>
                            </configuration>
                        </configuration>
                        <!-- provides JSR88 client API to deploy on Glassfish/Payara Server -->
                        <dependencies>
                            <dependency>
                                <groupId>org.glassfish.main.deployment</groupId>
                                <artifactId>deployment-client</artifactId>
                                <version>${glassfish.version}</version>
                            </dependency>
                            <dependency>
                                <groupId>org.glassfish.jaxb</groupId>
                                <artifactId>jaxb-runtime</artifactId>
                                <version>2.3.5</version>
                            </dependency>
                        </dependencies>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>arq-payara-embedded</id>
            <properties>
                <skipTests>false</skipTests>
            </properties>
            <dependencies>
                <dependency>
                    <groupId>fish.payara.extras</groupId>
                    <artifactId>payara-embedded-all</artifactId>
                    <version>${payara.version}</version>
                    <scope>test</scope>
                </dependency>
                <dependency>
                    <groupId>fish.payara.arquillian</groupId>
                    <artifactId>arquillian-payara-server-embedded</artifactId>
                    <version>${arquillian-payara.version}</version>
                    <scope>test</scope>
                </dependency>
            </dependencies>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-failsafe-plugin</artifactId>
                        <version>${maven-failsafe-plugin.version}</version>
                        <configuration>
                            <!-- This needs tuning -->
                            <systemPropertyVariables>
                                <arquillian.launch>glassfish</arquillian.launch>
                            </systemPropertyVariables>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>arq-payara-managed</id>
            <properties>
                <skipTests>false</skipTests>
            </properties>
            <dependencies>
                <!-- https://mvnrepository.com/artifact/fish.payara.arquillian/payara-client-ee8 -->
                <!-- Required since arquillian-payara 2.4 -->     
                <dependency>
                    <groupId>fish.payara.arquillian</groupId>
                    <artifactId>payara-client-ee8</artifactId>
                    <version>${arquillian-payara.version}</version>
                </dependency>     
                <dependency>
                    <groupId>fish.payara.arquillian</groupId>
                    <artifactId>arquillian-payara-server-managed</artifactId>
                    <version>${arquillian-payara.version}</version>
                    <scope>test</scope>
                </dependency>
            </dependencies>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-dependency-plugin</artifactId>
                        <version>${maven-dependency-plugin.version}</version>
                        <executions>
                            <execution>
                                <id>unpack</id>
                                <phase>process-test-classes</phase>
                                <goals>
                                    <goal>unpack</goal>
                                </goals>
                                <configuration>
                                    <artifactItems>
                                        <artifactItem>
                                            <groupId>fish.payara.distributions</groupId>
                                            <artifactId>payara</artifactId>
                                            <version>${payara.version}</version>
                                            <type>zip</type>
                                            <overWrite>false</overWrite>
                                            <outputDirectory>${project.build.directory}</outputDirectory>
                                        </artifactItem>
                                    </artifactItems>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-failsafe-plugin</artifactId>
                        <version>${maven-failsafe-plugin.version}</version>
                        <configuration>
                            <systemPropertyVariables>
                                <payara.home>${project.build.directory}/payara5</payara.home>
                                <arquillian.launch>glassfish</arquillian.launch>
                            </systemPropertyVariables>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>

        <profile>
            <id>arq-payara-remote</id>
            <properties>
                <skipTests>false</skipTests>
            </properties>
            <dependencies>
                <dependency>
                    <groupId>fish.payara.arquillian</groupId>
                    <artifactId>arquillian-payara-server-remote</artifactId>
                    <version>${arquillian-payara.version}</version>
                    <scope>test</scope>
                </dependency>
            </dependencies>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-failsafe-plugin</artifactId>
                        <version>${maven-failsafe-plugin.version}</version>
                        <configuration>
                            <!-- This needs tuning -->
                            <systemPropertyVariables>
                                <arquillian.launch>glassfish</arquillian.launch>
                            </systemPropertyVariables>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>
    <reporting>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-report-plugin</artifactId>
                <version>${maven-surefire-report-plugin.version}</version>
            </plugin>
        </plugins>
    </reporting>
</project>

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/README.md
# Initial
mvn clean wildfly:run -Pwildfly
mvn clean wildfly:run -Pwildfly -e
# Akses
https://hantsy.medium.com/put-your-jakarta-ee-8-applications-to-production-77756d1967bf
$curl http://localhost:8080/jakartaee8-starter/api/greeting/Hantsy
{"message":"Say Hello to Hantsy at 2020-03-09T07:57:13.634"}

http://172.21.37.37:9990/console/index.html#deployments;path=deployment~dply-jakartaee-jaxrs-samplewar
Name:          jakartaee-jaxrs-sample.war
Runtime Name:  jakartaee-jaxrs-sample.war
Context Root:  /jakartaee-jaxrs-sample

http://172.21.37.37:8080/jakartaee-jaxrs-sample/api/greeting/usef
RESTEASY003210: Could not find resource for full path: http://172.21.37.37:8080/jakartaee-jaxrs-sample/api/greeting/usef

usef@DESKTOP-7EO5LQL:/mnt/c/Users/user$ curl http://localhost:8080/jakartaee-jaxrs-sample
usef@DESKTOP-7EO5LQL:/mnt/c/Users/user$ curl http://localhost:8080/jakartaee-jaxrs-sample/api/greeting/usef
RESTEASY003210: Could not find resource for full path: http://localhost:8080/jakartaee-jaxrs-sample/api/greeting/usefusef@DESKTOP-7EO5LQL:/mnt/c/Users/user$

# Log
10:36:35,273 WARN  [org.jboss.as.jaxrs] (MSC service thread 1-4) WFLYRS0018: Explicit usage of Jackson annotation in a JAX-RS deployment; the system will disable JSON-B processing for the current deployment. Consider setting the 'resteasy.preferJacksonOverJsonB' property to 'false' to restore JSON-B.

== 

jboss_1  | 03:26:56,554 WARN  [io.undertow.servlet] (ServerService Thread Pool -- 76) UT015020: Path /api/users/* is secured for some HTTP methods, however it is not secured for [TRACE, HEAD, GET, CONNECT, OPTIONS]
jboss_1  | 03:26:56,555 WARN  [io.undertow.servlet] (ServerService Thread Pool -- 76) UT015020: Path /api/tasks/* is secured for some HTTP methods, however it is not secured for [TRACE, HEAD, GET, CONNECT, OPTIONS]
jboss_1  | 03:26:56,876 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 76) RESTEASY002225: Deploying javax.ws.rs.core.Application: class com.example.interfaces.RestConfiguration
jboss_1  | 03:26:56,979 INFO  [org.wildfly.extension.undertow] (ServerService Thread Pool -- 76) WFLYUT0021: Registered web context: '/jakartaee-jaxrs-sample' for server 'default-server'
jboss_1  | 03:26:57,076 INFO  [org.jboss.as.server] (ServerService Thread Pool -- 44) WFLYSRV0010: Deployed "jakartaee-jaxrs-sample.war" (runtime-name : "jakartaee-jaxrs-sample.war")

jboss_1  | 03:28:34,707 ERROR [io.undertow.request] (default task-1) UT005023: Exception handling request to /jakartaee-jaxrs-sample/api/users: org.jboss.resteasy.spi.UnhandledException: com.fasterxml.jackson.databind.JsonMappingException: failed to lazily initialize a collection of role: com.example.domain.user.User.authorities, could not initialize proxy - no Session (through reference chain: java.util.ArrayList[0]->com.example.domain.user.User["authorities"])

com.example.domain.user.User.authorities

https://stackoverflow.com/questions/22821695/how-to-fix-hibernate-lazyinitializationexception-failed-to-lazily-initialize-a

# Errors vs Ok

$ curl http://localhost:8080/jakartaee-jaxrs-sample/api/tasks
{"content":[{"id":1,"version":0,"createdDate":{"nano":741621000,"year":2022,"monthValue":1,"dayOfMonth":15,"hour":3,"minute":39,"second":50,"dayOfWeek":"SATURDAY","dayOfYear":15,"month":"JANUARY","chronology":{"calendarType":"iso8601","id":"ISO"}},"lastModifiedDate":{"nano":741621000,"year":2022,"monthValue":1,"dayOfMonth":15,"hour":3,"minute":39,"second":50,"dayOfWeek":"SATURDAY","dayOfYear":15,"month":"JANUARY","chronology":{"calendarType":"iso8601","id":"ISO"}},"createdBy":null,"lastModifiedBy":null,"name":"My first task","description":"The description of my first task","status":"TODO"},{"id":2,"version":0,"createdDate":{"nano":774835000,"year":2022,"monthValue":1,"dayOfMonth":15,"hour":3,"minute":39,"second":50,"dayOfWeek":"SATURDAY","dayOfYear":15,"month":"JANUARY","chronology":{"calendarType":"iso8601","id":"ISO"}},"lastModifiedDate":{"nano":774835000,"year":2022,"monthValue":1,"dayOfMonth":15,"hour":3,"minute":39,"second":50,"dayOfWeek":"SATURDAY","dayOfYear":15,"month":"JANUARY","chronology":{"calendarType":"iso8601","id":"ISO"}},"createdBy":null,"lastModifiedBy":null,"name":"My second task","description":"The description of my second task","status":"TODO"}],"count":2}


http://172.21.37.37:8080/jakartaee-jaxrs-sample/api/tasks

$ curl http://localhost:8080/jakartaee-jaxrs-sample/api/users
<html><head><title>Error</title></head><body>Internal Server Error</body></html>

# now

## after:
import javax.persistence.FetchType;
    // https://stackoverflow.com/questions/22821695/how-to-fix-hibernate-lazyinitializationexception-failed-to-lazily-initialize-a

    // @ElementCollection()
    @ElementCollection(fetch = FetchType.EAGER)
    private Set<String> authorities = new HashSet<>();
dan
main/resources/META-INF/persistence.xml
    <properties>
      <property name="javax.persistence.schema-generation.database.action" value="drop-and-create"/>
      <property name="hibernate.enable_lazy_load_no_trans" value="true" />
    </properties>

http://172.21.37.37:8080/jakartaee-jaxrs-sample/api/users
[{"id":3,"version":0,"username":"user","password":"$2a$10$.XVeK18ZIfUxIA5wRv3wTeACv6wc/n7oiKkC//874dpVYgoEhdwqy","firstName":"user firstName","lastName":"user lastName","email":"user@example.com","authorities":["ROLE_USER"]},{"id":4,"version":0,"username":"admin","password":"$2a$10$i9BpEcGBM2puJ.CyyZIeXOWT6GnfNR9G4YVWda1BUIZpCVFcZMDRW","firstName":"admin firstName","lastName":"admin lastName","email":"admin@example.com","authorities":["ROLE_USER","ROLE_ADMIN"]}]

#  Jakarta EE JAXRS Sample

![compile and build](https://github.com/hantsy/jakartaee-jaxrs-sample/workflows/build/badge.svg)
![Integration Test with Arquillian Payara Managed Container](https://github.com/hantsy/jakartaee-jaxrs-sample/workflows/it-with-arq-payara-managed/badge.svg)


A Jakarta Restful Web Service Sample application based on the [Jakarta EE 8 Starter](https://github.com/hantsy/jakartaee8-starter-boilerplate) boilerplate.

This project is the successor of [Java EE 8 Jaxrs Sample](https://github.com/hantsy/javaee8-jaxrs-sample) and [Java EE 7 Jaxrs Sample](https://github.com/hantsy/ee7-jaxrs-sample), and updated to the new Jakarta EE 8 API, including:

* Jakarta Restful Web Service
* Jakarta Enterprise Beans/Jakarta Persistence/Jakarta Bean Validation
* Jakarta Context and Dependency Injection
* Jakarta Security Enterprise API
* Microprofile Config API

> Note: In this sample, I upgraded the codebase to Java 11  and used the latest Payara 5 to run the application by default. 


## Build

1. Clone a copy of the source codes.

   ```bash
   git clone https://github.com/hantsy/jakartaee-jaxrs-sample
   ```

2. Run on Payara, WildFly or Open Liberty.

   ```bash
   mvn clean package cargo:run -Ppayara-local
   //or deploy to a running payara server
   mvn clean package cargo:deploy -Ppayara-remote
   
   //run on Wildfly server
   mvn clean wildfly:run -Pwildfly
   
   //run on Open Liberty
   mvn clean liberty:create dependency:copy liberty:run -Popenliberty
   ```
   
## Reference

* [Securing JAX-RS Endpoints with JWT](https://antoniogoncalves.org/2016/10/03/securing-jax-rs-endpoints-with-jwt/)
* [Java EE Security Essentials](https://dzone.com/refcardz/getting-started-java-ee?chapter=1)
* [JAX-RS, JWT & a pinch of JSR 375](https://abhirockzz.wordpress.com/2016/03/21/jax-rs-jwt-a-pinch-of-jsr-375/)
* [JSON Web Token in action with JAX-RS](https://abhirockzz.wordpress.com/2016/03/18/json-web-token-in-action-with-jax-rs/)
* [Java Magazine Hub](https://java-magazine-hub.zeef.com/)
* [Efficient JAX-RS: Conditional GETs & PUTs](https://abhirockzz.wordpress.com/2016/03/27/efficient-jax-rs-conditional-gets-puts/)
* [Java EE Security API - Soteria](https://www.n-k.de/2018/07/java-ee-security-api-jsr-375-soteria.html)

  

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/run.sh
mvn clean wildfly:run -Pwildfly -e
docker-compose up

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/dependabot.yml
version: 2
updates:
- package-ecosystem: github-actions
  directory: "/"
  schedule:
    interval: weekly
#    time: "21:00"
- package-ecosystem: maven
  directory: "/"
  schedule:
    interval: weekly
    time: "21:00"
  open-pull-requests-limit: 10
  # Overwrite any ignores created using `@dependabot ignore` commands
  ignore:
    # Ignore updates to packages that start 'aws'
    # Wildcards match zero or more arbitrary characters
    #- dependency-name: "aws*"
    # Ignore some updates to the 'resteasy' package
    - dependency-name: "resteasy"
      # Ignore only new versions for 4.x
      versions: ["3.x, 4.x"]
    - dependency-name: "jakarta.jakartaee-api"
    - dependency-name: "glassfish"
    - dependency-name: "jersey"
    - dependency-name: "eclipselink"
          

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/ISSUE_TEMPLATE/bug_report.md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: hantsy

---

Firstly make sure you are using Java 8 and Maven 3.1+ for building this project. 

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Additional context**
Add any other context about the problem here.

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/workflows/it-with-arq-payara-managed.yml
name: it-with-arq-payara-managed

on:
  push:
    paths-ignore:
      - "docs/**"
    branches:
      - master
  pull_request:
    types:
      - opened
      - synchronize
      - reopened

jobs:
  it-with-arq-payara-managed:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up JDK
        uses: actions/setup-java@v2.5.0
        with:
          java-version: 11
          distribution: 'adopt'

      - name: Cache Maven packages
        uses: actions/cache@v2
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2

      - name: Run integration test with -Parq-payara-managed
        run: mvn clean verify -Parq-payara-managed

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/.github/workflows/maven.yml
name: build

on: 
  push:
    branches:
    - master
    - release/*
  pull_request:
    branches:
    - master  
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - name: Set up JDK 11
      uses: actions/setup-java@v2.5.0
      with:
        java-version: 11
        distribution: 'adopt'
    - name: Build with Maven
      run: mvn clean package --file pom.xml
 
  automerge:
      name: Merge pull request
      runs-on: ubuntu-latest
      needs: [build]
      if: github.base_ref == 'master' && github.actor == 'dependabot[bot]'
      steps:
        - name: Merge
          uses: actions/github-script@v5
          with:
            script: |
              github.pulls.merge({
                owner: context.payload.repository.owner.login,
                repo: context.payload.repository.name,
                pull_number: context.payload.pull_request.number
              })
            github-token: ${{ secrets.GITHUB_TOKEN }}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/LoggerProducer.java
package com.example.application.util;

import java.util.logging.Logger;
import javax.enterprise.context.Dependent;
import javax.enterprise.inject.Produces;
import javax.enterprise.inject.spi.InjectionPoint;

/**
 *
 * @author hantsy
 */
@Dependent
public class LoggerProducer {

    @Produces
    public Logger getLogger(InjectionPoint p) {
        return Logger.getLogger(p.getMember().getDeclaringClass().getName());
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/SampleDataPopulator.java
package com.example.application.util;

import com.example.domain.task.Task;
import com.example.domain.task.TaskRepository;
import com.example.domain.user.User;
import com.example.domain.user.UserRepository;
import com.example.application.util.hash.Crypto;
import com.example.application.util.hash.PasswordEncoder;

import javax.annotation.PostConstruct;
import javax.ejb.Singleton;
import javax.ejb.Startup;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static com.example.infrastructure.security.SecurityConstant.ROLE_ADMIN;
import static com.example.infrastructure.security.SecurityConstant.ROLE_USER;

/**
 * @author hantsy
 */
@Startup
@Singleton
public class SampleDataPopulator {
    
    @Inject
    Logger LOG;
    
    @Inject
    TaskRepository tasks;
    
    @Inject
    UserRepository users;
    
    @Inject
    @Crypto(Crypto.Type.BCRYPT)
    PasswordEncoder passwordHash;
    
    @PersistenceContext
    EntityManager entityManager;
    
    @PostConstruct
    public void init() {
        initTasks();
        initUsers();
    }
    
    public void initTasks() {
        LOG.log(Level.INFO, " >> initializing tasks ...");
        
        var deleted = this.entityManager.createQuery("delete from Task").executeUpdate();
        LOG.log(Level.INFO, " deleted existed tasks: {0}", new Object[]{deleted});
        
        Stream.of("first", "second")
                .map(s -> {
                    Task task = new Task();
                    task.setName("My " + s + " task");
                    task.setDescription("The description of my " + s + " task");
                    task.setStatus(Task.Status.TODO);
                    return task;
                })
                .map(data -> tasks.save(data))
                .collect(Collectors.toList())
                .forEach(task -> LOG.log(Level.INFO, "saved task: {0}", new Object[]{task}));
    }
    
    public void initUsers() {
        LOG.log(Level.INFO, " >> initializing users ...");
        
        var deleted = this.entityManager.createQuery("delete from User").executeUpdate();
        LOG.log(Level.INFO, " deleted existed users: {0}", new Object[]{deleted});
        
        var user = User.builder()
                .username("user")
                .password(passwordHash.encode("password"))
                .firstName("user firstName")
                .lastName("user lastName")
                .email("user@example.com")
                .authorities(Set.of(ROLE_USER))
                .build();
        
        var admin = User.builder()
                .username("admin")
                .password(passwordHash.encode("password"))
                .firstName("admin firstName")
                .lastName("admin lastName")
                .email("admin@example.com")
                .authorities(Set.of(ROLE_USER, ROLE_ADMIN))
                .build();
        
        Stream.of(user, admin)
                .map(u -> users.save(u))
                .collect(Collectors.toList())
                .forEach(u -> LOG.log(Level.INFO, "saved user: {0}", new Object[]{u}));
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/Crypto.java
package com.example.application.util.hash;

import javax.enterprise.util.Nonbinding;
import javax.inject.Qualifier;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

/**
 *
 * @author hantsy
 */
@Qualifier
@Retention(RUNTIME)
@Target({METHOD, FIELD, PARAMETER, TYPE})
public @interface Crypto {

    enum Type {
        PLAIN, BCRYPT
    }

    @Nonbinding Type value() default Type.PLAIN;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/PasswordEncoder.java
package com.example.application.util.hash;

/**
 * @author hantsy
 */
public interface PasswordEncoder {

    String encode(CharSequence rawPassword);

    boolean matches(CharSequence rawPassword, String encodedPassword);

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/PasswordEncoderProducer.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.application.util.hash;



import com.example.application.util.hash.bcrypt.BCryptPasswordEncoder;
import com.example.application.util.hash.plain.PlainPasswordEncoder;

import javax.enterprise.context.Dependent;
import javax.enterprise.inject.Produces;
import javax.enterprise.inject.spi.InjectionPoint;

/**
 *
 * @author hantsy
 */
@Dependent
public class PasswordEncoderProducer {

    @Produces
    @Crypto
    public PasswordEncoder passwordEncoder(InjectionPoint ip) {
        Crypto crypto = ip.getAnnotated().getAnnotation(Crypto.class);
        Crypto.Type type = crypto.value();
        PasswordEncoder encoder;
        switch (type) {
            case BCRYPT:
                encoder = new BCryptPasswordEncoder();
                break;
            default:
                encoder = new PlainPasswordEncoder();
                break;
        }

        return encoder;
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/BCrypt.java
// Copyright (c) 2006 Damien Miller <djm@mindrot.org>
//
// Permission to use, copy, modify, and distribute this software for any
// purpose with or without fee is hereby granted, provided that the above
// copyright notice and this permission notice appear in all copies.
//
// THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
// WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
// MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
// ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
// WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
// ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
// OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
package com.example.application.util.hash.bcrypt;

import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.security.SecureRandom;

/**
 * BCrypt implements OpenBSD-style Blowfish password hashing using the scheme described in
 * "A Future-Adaptable Password Scheme" by Niels Provos and David Mazieres.
 * <p>
 * This password hashing system tries to thwart off-line password cracking using a
 * computationally-intensive hashing algorithm, based on Bruce Schneier's Blowfish cipher.
 * The work factor of the algorithm is parameterised, so it can be increased as computers
 * get faster.
 * <p>
 * Usage is really simple. To hash a password for the first time, call the hashpw method
 * with a random salt, like this:
 * <p>
 * <code>
 * String pw_hash = BCrypt.hashpw(plain_password, BCrypt.gensalt()); <br>
 * </code>
 * <p>
 * To check whether a plaintext password matches one that has been hashed previously, use
 * the checkpw method:
 * <p>
 * <code>
 * if (BCrypt.checkpw(candidate_password, stored_hash))<br>
 * &nbsp;&nbsp;&nbsp;&nbsp;System.out.println("It matches");<br>
 * else<br>
 * &nbsp;&nbsp;&nbsp;&nbsp;System.out.println("It does not match");<br>
 * </code>
 * <p>
 * The gensalt() method takes an optional parameter (log_rounds) that determines the
 * computational complexity of the hashing:
 * <p>
 * <code>
 * String strong_salt = BCrypt.gensalt(10)<br>
 * String stronger_salt = BCrypt.gensalt(12)<br>
 * </code>
 * <p>
 * The amount of work increases exponentially (2**log_rounds), so each increment is twice
 * as much work. The default log_rounds is 10, and the valid range is 4 to 31.
 *
 * @author Damien Miller
 */
public class BCrypt {
	// BCrypt parameters

	private static final int GENSALT_DEFAULT_LOG2_ROUNDS = 10;
	private static final int BCRYPT_SALT_LEN = 16;
	// Blowfish parameters
	private static final int BLOWFISH_NUM_ROUNDS = 16;
	// Initial contents of key schedule
	private static final int P_orig[] = { 0x243f6a88, 0x85a308d3, 0x13198a2e, 0x03707344,
			0xa4093822, 0x299f31d0, 0x082efa98, 0xec4e6c89, 0x452821e6, 0x38d01377,
			0xbe5466cf, 0x34e90c6c, 0xc0ac29b7, 0xc97c50dd, 0x3f84d5b5, 0xb5470917,
			0x9216d5d9, 0x8979fb1b };
	private static final int S_orig[] = { 0xd1310ba6, 0x98dfb5ac, 0x2ffd72db, 0xd01adfb7,
			0xb8e1afed, 0x6a267e96, 0xba7c9045, 0xf12c7f99, 0x24a19947, 0xb3916cf7,
			0x0801f2e2, 0x858efc16, 0x636920d8, 0x71574e69, 0xa458fea3, 0xf4933d7e,
			0x0d95748f, 0x728eb658, 0x718bcd58, 0x82154aee, 0x7b54a41d, 0xc25a59b5,
			0x9c30d539, 0x2af26013, 0xc5d1b023, 0x286085f0, 0xca417918, 0xb8db38ef,
			0x8e79dcb0, 0x603a180e, 0x6c9e0e8b, 0xb01e8a3e, 0xd71577c1, 0xbd314b27,
			0x78af2fda, 0x55605c60, 0xe65525f3, 0xaa55ab94, 0x57489862, 0x63e81440,
			0x55ca396a, 0x2aab10b6, 0xb4cc5c34, 0x1141e8ce, 0xa15486af, 0x7c72e993,
			0xb3ee1411, 0x636fbc2a, 0x2ba9c55d, 0x741831f6, 0xce5c3e16, 0x9b87931e,
			0xafd6ba33, 0x6c24cf5c, 0x7a325381, 0x28958677, 0x3b8f4898, 0x6b4bb9af,
			0xc4bfe81b, 0x66282193, 0x61d809cc, 0xfb21a991, 0x487cac60, 0x5dec8032,
			0xef845d5d, 0xe98575b1, 0xdc262302, 0xeb651b88, 0x23893e81, 0xd396acc5,
			0x0f6d6ff3, 0x83f44239, 0x2e0b4482, 0xa4842004, 0x69c8f04a, 0x9e1f9b5e,
			0x21c66842, 0xf6e96c9a, 0x670c9c61, 0xabd388f0, 0x6a51a0d2, 0xd8542f68,
			0x960fa728, 0xab5133a3, 0x6eef0b6c, 0x137a3be4, 0xba3bf050, 0x7efb2a98,
			0xa1f1651d, 0x39af0176, 0x66ca593e, 0x82430e88, 0x8cee8619, 0x456f9fb4,
			0x7d84a5c3, 0x3b8b5ebe, 0xe06f75d8, 0x85c12073, 0x401a449f, 0x56c16aa6,
			0x4ed3aa62, 0x363f7706, 0x1bfedf72, 0x429b023d, 0x37d0d724, 0xd00a1248,
			0xdb0fead3, 0x49f1c09b, 0x075372c9, 0x80991b7b, 0x25d479d8, 0xf6e8def7,
			0xe3fe501a, 0xb6794c3b, 0x976ce0bd, 0x04c006ba, 0xc1a94fb6, 0x409f60c4,
			0x5e5c9ec2, 0x196a2463, 0x68fb6faf, 0x3e6c53b5, 0x1339b2eb, 0x3b52ec6f,
			0x6dfc511f, 0x9b30952c, 0xcc814544, 0xaf5ebd09, 0xbee3d004, 0xde334afd,
			0x660f2807, 0x192e4bb3, 0xc0cba857, 0x45c8740f, 0xd20b5f39, 0xb9d3fbdb,
			0x5579c0bd, 0x1a60320a, 0xd6a100c6, 0x402c7279, 0x679f25fe, 0xfb1fa3cc,
			0x8ea5e9f8, 0xdb3222f8, 0x3c7516df, 0xfd616b15, 0x2f501ec8, 0xad0552ab,
			0x323db5fa, 0xfd238760, 0x53317b48, 0x3e00df82, 0x9e5c57bb, 0xca6f8ca0,
			0x1a87562e, 0xdf1769db, 0xd542a8f6, 0x287effc3, 0xac6732c6, 0x8c4f5573,
			0x695b27b0, 0xbbca58c8, 0xe1ffa35d, 0xb8f011a0, 0x10fa3d98, 0xfd2183b8,
			0x4afcb56c, 0x2dd1d35b, 0x9a53e479, 0xb6f84565, 0xd28e49bc, 0x4bfb9790,
			0xe1ddf2da, 0xa4cb7e33, 0x62fb1341, 0xcee4c6e8, 0xef20cada, 0x36774c01,
			0xd07e9efe, 0x2bf11fb4, 0x95dbda4d, 0xae909198, 0xeaad8e71, 0x6b93d5a0,
			0xd08ed1d0, 0xafc725e0, 0x8e3c5b2f, 0x8e7594b7, 0x8ff6e2fb, 0xf2122b64,
			0x8888b812, 0x900df01c, 0x4fad5ea0, 0x688fc31c, 0xd1cff191, 0xb3a8c1ad,
			0x2f2f2218, 0xbe0e1777, 0xea752dfe, 0x8b021fa1, 0xe5a0cc0f, 0xb56f74e8,
			0x18acf3d6, 0xce89e299, 0xb4a84fe0, 0xfd13e0b7, 0x7cc43b81, 0xd2ada8d9,
			0x165fa266, 0x80957705, 0x93cc7314, 0x211a1477, 0xe6ad2065, 0x77b5fa86,
			0xc75442f5, 0xfb9d35cf, 0xebcdaf0c, 0x7b3e89a0, 0xd6411bd3, 0xae1e7e49,
			0x00250e2d, 0x2071b35e, 0x226800bb, 0x57b8e0af, 0x2464369b, 0xf009b91e,
			0x5563911d, 0x59dfa6aa, 0x78c14389, 0xd95a537f, 0x207d5ba2, 0x02e5b9c5,
			0x83260376, 0x6295cfa9, 0x11c81968, 0x4e734a41, 0xb3472dca, 0x7b14a94a,
			0x1b510052, 0x9a532915, 0xd60f573f, 0xbc9bc6e4, 0x2b60a476, 0x81e67400,
			0x08ba6fb5, 0x571be91f, 0xf296ec6b, 0x2a0dd915, 0xb6636521, 0xe7b9f9b6,
			0xff34052e, 0xc5855664, 0x53b02d5d, 0xa99f8fa1, 0x08ba4799, 0x6e85076a,
			0x4b7a70e9, 0xb5b32944, 0xdb75092e, 0xc4192623, 0xad6ea6b0, 0x49a7df7d,
			0x9cee60b8, 0x8fedb266, 0xecaa8c71, 0x699a17ff, 0x5664526c, 0xc2b19ee1,
			0x193602a5, 0x75094c29, 0xa0591340, 0xe4183a3e, 0x3f54989a, 0x5b429d65,
			0x6b8fe4d6, 0x99f73fd6, 0xa1d29c07, 0xefe830f5, 0x4d2d38e6, 0xf0255dc1,
			0x4cdd2086, 0x8470eb26, 0x6382e9c6, 0x021ecc5e, 0x09686b3f, 0x3ebaefc9,
			0x3c971814, 0x6b6a70a1, 0x687f3584, 0x52a0e286, 0xb79c5305, 0xaa500737,
			0x3e07841c, 0x7fdeae5c, 0x8e7d44ec, 0x5716f2b8, 0xb03ada37, 0xf0500c0d,
			0xf01c1f04, 0x0200b3ff, 0xae0cf51a, 0x3cb574b2, 0x25837a58, 0xdc0921bd,
			0xd19113f9, 0x7ca92ff6, 0x94324773, 0x22f54701, 0x3ae5e581, 0x37c2dadc,
			0xc8b57634, 0x9af3dda7, 0xa9446146, 0x0fd0030e, 0xecc8c73e, 0xa4751e41,
			0xe238cd99, 0x3bea0e2f, 0x3280bba1, 0x183eb331, 0x4e548b38, 0x4f6db908,
			0x6f420d03, 0xf60a04bf, 0x2cb81290, 0x24977c79, 0x5679b072, 0xbcaf89af,
			0xde9a771f, 0xd9930810, 0xb38bae12, 0xdccf3f2e, 0x5512721f, 0x2e6b7124,
			0x501adde6, 0x9f84cd87, 0x7a584718, 0x7408da17, 0xbc9f9abc, 0xe94b7d8c,
			0xec7aec3a, 0xdb851dfa, 0x63094366, 0xc464c3d2, 0xef1c1847, 0x3215d908,
			0xdd433b37, 0x24c2ba16, 0x12a14d43, 0x2a65c451, 0x50940002, 0x133ae4dd,
			0x71dff89e, 0x10314e55, 0x81ac77d6, 0x5f11199b, 0x043556f1, 0xd7a3c76b,
			0x3c11183b, 0x5924a509, 0xf28fe6ed, 0x97f1fbfa, 0x9ebabf2c, 0x1e153c6e,
			0x86e34570, 0xeae96fb1, 0x860e5e0a, 0x5a3e2ab3, 0x771fe71c, 0x4e3d06fa,
			0x2965dcb9, 0x99e71d0f, 0x803e89d6, 0x5266c825, 0x2e4cc978, 0x9c10b36a,
			0xc6150eba, 0x94e2ea78, 0xa5fc3c53, 0x1e0a2df4, 0xf2f74ea7, 0x361d2b3d,
			0x1939260f, 0x19c27960, 0x5223a708, 0xf71312b6, 0xebadfe6e, 0xeac31f66,
			0xe3bc4595, 0xa67bc883, 0xb17f37d1, 0x018cff28, 0xc332ddef, 0xbe6c5aa5,
			0x65582185, 0x68ab9802, 0xeecea50f, 0xdb2f953b, 0x2aef7dad, 0x5b6e2f84,
			0x1521b628, 0x29076170, 0xecdd4775, 0x619f1510, 0x13cca830, 0xeb61bd96,
			0x0334fe1e, 0xaa0363cf, 0xb5735c90, 0x4c70a239, 0xd59e9e0b, 0xcbaade14,
			0xeecc86bc, 0x60622ca7, 0x9cab5cab, 0xb2f3846e, 0x648b1eaf, 0x19bdf0ca,
			0xa02369b9, 0x655abb50, 0x40685a32, 0x3c2ab4b3, 0x319ee9d5, 0xc021b8f7,
			0x9b540b19, 0x875fa099, 0x95f7997e, 0x623d7da8, 0xf837889a, 0x97e32d77,
			0x11ed935f, 0x16681281, 0x0e358829, 0xc7e61fd6, 0x96dedfa1, 0x7858ba99,
			0x57f584a5, 0x1b227263, 0x9b83c3ff, 0x1ac24696, 0xcdb30aeb, 0x532e3054,
			0x8fd948e4, 0x6dbc3128, 0x58ebf2ef, 0x34c6ffea, 0xfe28ed61, 0xee7c3c73,
			0x5d4a14d9, 0xe864b7e3, 0x42105d14, 0x203e13e0, 0x45eee2b6, 0xa3aaabea,
			0xdb6c4f15, 0xfacb4fd0, 0xc742f442, 0xef6abbb5, 0x654f3b1d, 0x41cd2105,
			0xd81e799e, 0x86854dc7, 0xe44b476a, 0x3d816250, 0xcf62a1f2, 0x5b8d2646,
			0xfc8883a0, 0xc1c7b6a3, 0x7f1524c3, 0x69cb7492, 0x47848a0b, 0x5692b285,
			0x095bbf00, 0xad19489d, 0x1462b174, 0x23820e00, 0x58428d2a, 0x0c55f5ea,
			0x1dadf43e, 0x233f7061, 0x3372f092, 0x8d937e41, 0xd65fecf1, 0x6c223bdb,
			0x7cde3759, 0xcbee7460, 0x4085f2a7, 0xce77326e, 0xa6078084, 0x19f8509e,
			0xe8efd855, 0x61d99735, 0xa969a7aa, 0xc50c06c2, 0x5a04abfc, 0x800bcadc,
			0x9e447a2e, 0xc3453484, 0xfdd56705, 0x0e1e9ec9, 0xdb73dbd3, 0x105588cd,
			0x675fda79, 0xe3674340, 0xc5c43465, 0x713e38d8, 0x3d28f89e, 0xf16dff20,
			0x153e21e7, 0x8fb03d4a, 0xe6e39f2b, 0xdb83adf7, 0xe93d5a68, 0x948140f7,
			0xf64c261c, 0x94692934, 0x411520f7, 0x7602d4f7, 0xbcf46b2e, 0xd4a20068,
			0xd4082471, 0x3320f46a, 0x43b7d4b7, 0x500061af, 0x1e39f62e, 0x97244546,
			0x14214f74, 0xbf8b8840, 0x4d95fc1d, 0x96b591af, 0x70f4ddd3, 0x66a02f45,
			0xbfbc09ec, 0x03bd9785, 0x7fac6dd0, 0x31cb8504, 0x96eb27b3, 0x55fd3941,
			0xda2547e6, 0xabca0a9a, 0x28507825, 0x530429f4, 0x0a2c86da, 0xe9b66dfb,
			0x68dc1462, 0xd7486900, 0x680ec0a4, 0x27a18dee, 0x4f3ffea2, 0xe887ad8c,
			0xb58ce006, 0x7af4d6b6, 0xaace1e7c, 0xd3375fec, 0xce78a399, 0x406b2a42,
			0x20fe9e35, 0xd9f385b9, 0xee39d7ab, 0x3b124e8b, 0x1dc9faf7, 0x4b6d1856,
			0x26a36631, 0xeae397b2, 0x3a6efa74, 0xdd5b4332, 0x6841e7f7, 0xca7820fb,
			0xfb0af54e, 0xd8feb397, 0x454056ac, 0xba489527, 0x55533a3a, 0x20838d87,
			0xfe6ba9b7, 0xd096954b, 0x55a867bc, 0xa1159a58, 0xcca92963, 0x99e1db33,
			0xa62a4a56, 0x3f3125f9, 0x5ef47e1c, 0x9029317c, 0xfdf8e802, 0x04272f70,
			0x80bb155c, 0x05282ce3, 0x95c11548, 0xe4c66d22, 0x48c1133f, 0xc70f86dc,
			0x07f9c9ee, 0x41041f0f, 0x404779a4, 0x5d886e17, 0x325f51eb, 0xd59bc0d1,
			0xf2bcc18f, 0x41113564, 0x257b7834, 0x602a9c60, 0xdff8e8a3, 0x1f636c1b,
			0x0e12b4c2, 0x02e1329e, 0xaf664fd1, 0xcad18115, 0x6b2395e0, 0x333e92e1,
			0x3b240b62, 0xeebeb922, 0x85b2a20e, 0xe6ba0d99, 0xde720c8c, 0x2da2f728,
			0xd0127845, 0x95b794fd, 0x647d0862, 0xe7ccf5f0, 0x5449a36f, 0x877d48fa,
			0xc39dfd27, 0xf33e8d1e, 0x0a476341, 0x992eff74, 0x3a6f6eab, 0xf4f8fd37,
			0xa812dc60, 0xa1ebddf8, 0x991be14c, 0xdb6e6b0d, 0xc67b5510, 0x6d672c37,
			0x2765d43b, 0xdcd0e804, 0xf1290dc7, 0xcc00ffa3, 0xb5390f92, 0x690fed0b,
			0x667b9ffb, 0xcedb7d9c, 0xa091cf0b, 0xd9155ea3, 0xbb132f88, 0x515bad24,
			0x7b9479bf, 0x763bd6eb, 0x37392eb3, 0xcc115979, 0x8026e297, 0xf42e312d,
			0x6842ada7, 0xc66a2b3b, 0x12754ccc, 0x782ef11c, 0x6a124237, 0xb79251e7,
			0x06a1bbe6, 0x4bfb6350, 0x1a6b1018, 0x11caedfa, 0x3d25bdd8, 0xe2e1c3c9,
			0x44421659, 0x0a121386, 0xd90cec6e, 0xd5abea2a, 0x64af674e, 0xda86a85f,
			0xbebfe988, 0x64e4c3fe, 0x9dbc8057, 0xf0f7c086, 0x60787bf8, 0x6003604d,
			0xd1fd8346, 0xf6381fb0, 0x7745ae04, 0xd736fccc, 0x83426b33, 0xf01eab71,
			0xb0804187, 0x3c005e5f, 0x77a057be, 0xbde8ae24, 0x55464299, 0xbf582e61,
			0x4e58f48f, 0xf2ddfda2, 0xf474ef38, 0x8789bdc2, 0x5366f9c3, 0xc8b38e74,
			0xb475f255, 0x46fcd9b9, 0x7aeb2661, 0x8b1ddf84, 0x846a0e79, 0x915f95e2,
			0x466e598e, 0x20b45770, 0x8cd55591, 0xc902de4c, 0xb90bace1, 0xbb8205d0,
			0x11a86248, 0x7574a99e, 0xb77f19b6, 0xe0a9dc09, 0x662d09a1, 0xc4324633,
			0xe85a1f02, 0x09f0be8c, 0x4a99a025, 0x1d6efe10, 0x1ab93d1d, 0x0ba5a4df,
			0xa186f20f, 0x2868f169, 0xdcb7da83, 0x573906fe, 0xa1e2ce9b, 0x4fcd7f52,
			0x50115e01, 0xa70683fa, 0xa002b5c4, 0x0de6d027, 0x9af88c27, 0x773f8641,
			0xc3604c06, 0x61a806b5, 0xf0177a28, 0xc0f586e0, 0x006058aa, 0x30dc7d62,
			0x11e69ed7, 0x2338ea63, 0x53c2dd94, 0xc2c21634, 0xbbcbee56, 0x90bcb6de,
			0xebfc7da1, 0xce591d76, 0x6f05e409, 0x4b7c0188, 0x39720a3d, 0x7c927c24,
			0x86e3725f, 0x724d9db9, 0x1ac15bb4, 0xd39eb8fc, 0xed545578, 0x08fca5b5,
			0xd83d7cd3, 0x4dad0fc4, 0x1e50ef5e, 0xb161e6f8, 0xa28514d9, 0x6c51133c,
			0x6fd5c7e7, 0x56e14ec4, 0x362abfce, 0xddc6c837, 0xd79a3234, 0x92638212,
			0x670efa8e, 0x406000e0, 0x3a39ce37, 0xd3faf5cf, 0xabc27737, 0x5ac52d1b,
			0x5cb0679e, 0x4fa33742, 0xd3822740, 0x99bc9bbe, 0xd5118e9d, 0xbf0f7315,
			0xd62d1c7e, 0xc700c47b, 0xb78c1b6b, 0x21a19045, 0xb26eb1be, 0x6a366eb4,
			0x5748ab2f, 0xbc946e79, 0xc6a376d2, 0x6549c2c8, 0x530ff8ee, 0x468dde7d,
			0xd5730a1d, 0x4cd04dc6, 0x2939bbdb, 0xa9ba4650, 0xac9526e8, 0xbe5ee304,
			0xa1fad5f0, 0x6a2d519a, 0x63ef8ce2, 0x9a86ee22, 0xc089c2b8, 0x43242ef6,
			0xa51e03aa, 0x9cf2d0a4, 0x83c061ba, 0x9be96a4d, 0x8fe51550, 0xba645bd6,
			0x2826a2f9, 0xa73a3ae1, 0x4ba99586, 0xef5562e9, 0xc72fefd3, 0xf752f7da,
			0x3f046f69, 0x77fa0a59, 0x80e4a915, 0x87b08601, 0x9b09e6ad, 0x3b3ee593,
			0xe990fd5a, 0x9e34d797, 0x2cf0b7d9, 0x022b8b51, 0x96d5ac3a, 0x017da67d,
			0xd1cf3ed6, 0x7c7d2d28, 0x1f9f25cf, 0xadf2b89b, 0x5ad6b472, 0x5a88f54c,
			0xe029ac71, 0xe019a5e6, 0x47b0acfd, 0xed93fa9b, 0xe8d3c48d, 0x283b57cc,
			0xf8d56629, 0x79132e28, 0x785f0191, 0xed756055, 0xf7960e44, 0xe3d35e8c,
			0x15056dd4, 0x88f46dba, 0x03a16125, 0x0564f0bd, 0xc3eb9e15, 0x3c9057a2,
			0x97271aec, 0xa93a072a, 0x1b3f6d9b, 0x1e6321f5, 0xf59c66fb, 0x26dcf319,
			0x7533d928, 0xb155fdf5, 0x03563482, 0x8aba3cbb, 0x28517711, 0xc20ad9f8,
			0xabcc5167, 0xccad925f, 0x4de81751, 0x3830dc8e, 0x379d5862, 0x9320f991,
			0xea7a90c2, 0xfb3e7bce, 0x5121ce64, 0x774fbe32, 0xa8b6e37e, 0xc3293d46,
			0x48de5369, 0x6413e680, 0xa2ae0810, 0xdd6db224, 0x69852dfd, 0x09072166,
			0xb39a460a, 0x6445c0dd, 0x586cdecf, 0x1c20c8ae, 0x5bbef7dd, 0x1b588d40,
			0xccd2017f, 0x6bb4e3bb, 0xdda26a7e, 0x3a59ff45, 0x3e350a44, 0xbcb4cdd5,
			0x72eacea8, 0xfa6484bb, 0x8d6612ae, 0xbf3c6f47, 0xd29be463, 0x542f5d9e,
			0xaec2771b, 0xf64e6370, 0x740e0d8d, 0xe75b1357, 0xf8721671, 0xaf537d5d,
			0x4040cb08, 0x4eb4e2cc, 0x34d2466a, 0x0115af84, 0xe1b00428, 0x95983a1d,
			0x06b89fb4, 0xce6ea048, 0x6f3f3b82, 0x3520ab82, 0x011a1d4b, 0x277227f8,
			0x611560b1, 0xe7933fdc, 0xbb3a792b, 0x344525bd, 0xa08839e1, 0x51ce794b,
			0x2f32c9b7, 0xa01fbac9, 0xe01cc87e, 0xbcc7d1f6, 0xcf0111c3, 0xa1e8aac7,
			0x1a908749, 0xd44fbd9a, 0xd0dadecb, 0xd50ada38, 0x0339c32a, 0xc6913667,
			0x8df9317c, 0xe0b12b4f, 0xf79e59b7, 0x43f5bb3a, 0xf2d519ff, 0x27d9459c,
			0xbf97222c, 0x15e6fc2a, 0x0f91fc71, 0x9b941525, 0xfae59361, 0xceb69ceb,
			0xc2a86459, 0x12baa8d1, 0xb6c1075e, 0xe3056a0c, 0x10d25065, 0xcb03a442,
			0xe0ec6e0e, 0x1698db3b, 0x4c98a0be, 0x3278e964, 0x9f1f9532, 0xe0d392df,
			0xd3a0342b, 0x8971f21e, 0x1b0a7441, 0x4ba3348c, 0xc5be7120, 0xc37632d8,
			0xdf359f8d, 0x9b992f2e, 0xe60b6f47, 0x0fe3f11d, 0xe54cda54, 0x1edad891,
			0xce6279cf, 0xcd3e7e6f, 0x1618b166, 0xfd2c1d05, 0x848fd2c5, 0xf6fb2299,
			0xf523f357, 0xa6327623, 0x93a83531, 0x56cccd02, 0xacf08162, 0x5a75ebb5,
			0x6e163697, 0x88d273cc, 0xde966292, 0x81b949d0, 0x4c50901b, 0x71c65614,
			0xe6c6c7bd, 0x327a140a, 0x45e1d006, 0xc3f27b9a, 0xc9aa53fd, 0x62a80f00,
			0xbb25bfe2, 0x35bdd2f6, 0x71126905, 0xb2040222, 0xb6cbcf7c, 0xcd769c2b,
			0x53113ec0, 0x1640e3d3, 0x38abbd60, 0x2547adf0, 0xba38209c, 0xf746ce76,
			0x77afa1c5, 0x20756060, 0x85cbfe4e, 0x8ae88dd8, 0x7aaaf9b0, 0x4cf9aa7e,
			0x1948c25c, 0x02fb8a8c, 0x01c36ae4, 0xd6ebe1f9, 0x90d4f869, 0xa65cdea0,
			0x3f09252d, 0xc208e69f, 0xb74e6132, 0xce77e25b, 0x578fdfe3, 0x3ac372e6 };
	// bcrypt IV: "OrpheanBeholderScryDoubt"
	static private final int bf_crypt_ciphertext[] = { 0x4f727068, 0x65616e42,
			0x65686f6c, 0x64657253, 0x63727944, 0x6f756274 };
	// Table for Base64 encoding
	static private final char base64_code[] = { '.', '/', 'A', 'B', 'C', 'D', 'E', 'F',
			'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
			'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
			'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
	// Table for Base64 decoding
	static private final byte index_64[] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
			-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
			-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 54, 55,
			56, 57, 58, 59, 60, 61, 62, 63, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, 6, 7,
			8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
			-1, -1, -1, -1, -1, -1, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
			41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, -1, -1, -1, -1, -1 };
	static final int MIN_LOG_ROUNDS = 4;
	static final int MAX_LOG_ROUNDS = 31;
	// Expanded Blowfish key
	private int P[];
	private int S[];

	/**
	 * Encode a byte array using bcrypt's slightly-modified base64 encoding scheme. Note
	 * that this is <strong>not</strong> compatible with the standard MIME-base64
	 * encoding.
	 *
	 * @param d the byte array to encode
	 * @param len the number of bytes to encode
	 * @param rs the destination buffer for the base64-encoded string
	 * @exception IllegalArgumentException if the length is invalid
	 */
	static void encode_base64(byte d[], int len, StringBuilder rs)
			throws IllegalArgumentException {
		int off = 0;
		int c1, c2;

		if (len <= 0 || len > d.length) {
			throw new IllegalArgumentException("Invalid len");
		}

		while (off < len) {
			c1 = d[off++] & 0xff;
			rs.append(base64_code[(c1 >> 2) & 0x3f]);
			c1 = (c1 & 0x03) << 4;
			if (off >= len) {
				rs.append(base64_code[c1 & 0x3f]);
				break;
			}
			c2 = d[off++] & 0xff;
			c1 |= (c2 >> 4) & 0x0f;
			rs.append(base64_code[c1 & 0x3f]);
			c1 = (c2 & 0x0f) << 2;
			if (off >= len) {
				rs.append(base64_code[c1 & 0x3f]);
				break;
			}
			c2 = d[off++] & 0xff;
			c1 |= (c2 >> 6) & 0x03;
			rs.append(base64_code[c1 & 0x3f]);
			rs.append(base64_code[c2 & 0x3f]);
		}
	}

	/**
	 * Look up the 3 bits base64-encoded by the specified character, range-checking
	 * against conversion table
	 * @param x the base64-encoded value
	 * @return the decoded value of x
	 */
	private static byte char64(char x) {
		if (x > index_64.length) {
			return -1;
		}
		return index_64[x];
	}

	/**
	 * Decode a string encoded using bcrypt's base64 scheme to a byte array. Note that
	 * this is *not* compatible with the standard MIME-base64 encoding.
	 * @param s the string to decode
	 * @param maxolen the maximum number of bytes to decode
	 * @return an array containing the decoded bytes
	 * @throws IllegalArgumentException if maxolen is invalid
	 */
	static byte[] decode_base64(String s, int maxolen) throws IllegalArgumentException {
		ByteArrayOutputStream out = new ByteArrayOutputStream(maxolen);
		int off = 0, slen = s.length(), olen = 0;
		byte c1, c2, c3, c4, o;

		if (maxolen <= 0) {
			throw new IllegalArgumentException("Invalid maxolen");
		}

		while (off < slen - 1 && olen < maxolen) {
			c1 = char64(s.charAt(off++));
			c2 = char64(s.charAt(off++));
			if (c1 == -1 || c2 == -1) {
				break;
			}
			o = (byte) (c1 << 2);
			o |= (c2 & 0x30) >> 4;
			out.write(o);
			if (++olen >= maxolen || off >= slen) {
				break;
			}
			c3 = char64(s.charAt(off++));
			if (c3 == -1) {
				break;
			}
			o = (byte) ((c2 & 0x0f) << 4);
			o |= (c3 & 0x3c) >> 2;
			out.write(o);
			if (++olen >= maxolen || off >= slen) {
				break;
			}
			c4 = char64(s.charAt(off++));
			o = (byte) ((c3 & 0x03) << 6);
			o |= c4;
			out.write(o);
			++olen;
		}

		return out.toByteArray();
	}

	/**
	 * Blowfish encipher a single 64-bit block encoded as two 32-bit halves
	 * @param lr an array containing the two 32-bit half blocks
	 * @param off the position in the array of the blocks
	 */
	private final void encipher(int lr[], int off) {
		int i, n, l = lr[off], r = lr[off + 1];

		l ^= P[0];
		for (i = 0; i <= BLOWFISH_NUM_ROUNDS - 2;) {
			// Feistel substitution on left word
			n = S[(l >> 24) & 0xff];
			n += S[0x100 | ((l >> 16) & 0xff)];
			n ^= S[0x200 | ((l >> 8) & 0xff)];
			n += S[0x300 | (l & 0xff)];
			r ^= n ^ P[++i];

			// Feistel substitution on right word
			n = S[(r >> 24) & 0xff];
			n += S[0x100 | ((r >> 16) & 0xff)];
			n ^= S[0x200 | ((r >> 8) & 0xff)];
			n += S[0x300 | (r & 0xff)];
			l ^= n ^ P[++i];
		}
		lr[off] = r ^ P[BLOWFISH_NUM_ROUNDS + 1];
		lr[off + 1] = l;
	}

	/**
	 * Cycically extract a word of key material
	 * @param data the string to extract the data from
	 * @param offp a "pointer" (as a one-entry array) to the current offset into data
	 * @return the next word of material from data
	 */
	private static int streamtoword(byte data[], int offp[]) {
		int i;
		int word = 0;
		int off = offp[0];

		for (i = 0; i < 4; i++) {
			word = (word << 8) | (data[off] & 0xff);
			off = (off + 1) % data.length;
		}

		offp[0] = off;
		return word;
	}

	/**
	 * Initialise the Blowfish key schedule
	 */
	private void init_key() {
		P = (int[]) P_orig.clone();
		S = (int[]) S_orig.clone();
	}

	/**
	 * Key the Blowfish cipher
	 * @param key an array containing the key
	 */
	private void key(byte key[]) {
		int i;
		int koffp[] = { 0 };
		int lr[] = { 0, 0 };
		int plen = P.length, slen = S.length;

		for (i = 0; i < plen; i++) {
			P[i] = P[i] ^ streamtoword(key, koffp);
		}

		for (i = 0; i < plen; i += 2) {
			encipher(lr, 0);
			P[i] = lr[0];
			P[i + 1] = lr[1];
		}

		for (i = 0; i < slen; i += 2) {
			encipher(lr, 0);
			S[i] = lr[0];
			S[i + 1] = lr[1];
		}
	}

	/**
	 * Perform the "enhanced key schedule" step described by Provos and Mazieres in
	 * "A Future-Adaptable Password Scheme" http://www.openbsd.org/papers/bcrypt-paper.ps
	 * @param data salt information
	 * @param key password information
	 */
	private void ekskey(byte data[], byte key[]) {
		int i;
		int koffp[] = { 0 }, doffp[] = { 0 };
		int lr[] = { 0, 0 };
		int plen = P.length, slen = S.length;

		for (i = 0; i < plen; i++) {
			P[i] = P[i] ^ streamtoword(key, koffp);
		}

		for (i = 0; i < plen; i += 2) {
			lr[0] ^= streamtoword(data, doffp);
			lr[1] ^= streamtoword(data, doffp);
			encipher(lr, 0);
			P[i] = lr[0];
			P[i + 1] = lr[1];
		}

		for (i = 0; i < slen; i += 2) {
			lr[0] ^= streamtoword(data, doffp);
			lr[1] ^= streamtoword(data, doffp);
			encipher(lr, 0);
			S[i] = lr[0];
			S[i + 1] = lr[1];
		}
	}

	static long roundsForLogRounds(int log_rounds) {
		if (log_rounds < 4 || log_rounds > 31) {
			throw new IllegalArgumentException("Bad number of rounds");
		}
		return 1L << log_rounds;
	}

	/**
	 * Perform the central password hashing step in the bcrypt scheme
	 * @param password the password to hash
	 * @param salt the binary salt to hash with the password
	 * @param log_rounds the binary logarithm of the number of rounds of hashing to apply
	 * @return an array containing the binary hashed password
	 */
	private byte[] crypt_raw(byte password[], byte salt[], int log_rounds) {
		int cdata[] = (int[]) bf_crypt_ciphertext.clone();
		int clen = cdata.length;
		byte ret[];

		long rounds = roundsForLogRounds(log_rounds);

		init_key();
		ekskey(salt, password);
		for (long i = 0; i < rounds; i++) {
			key(password);
			key(salt);
		}

		for (int i = 0; i < 64; i++) {
			for (int j = 0; j < (clen >> 1); j++) {
				encipher(cdata, j << 1);
			}
		}

		ret = new byte[clen * 4];
		for (int i = 0, j = 0; i < clen; i++) {
			ret[j++] = (byte) ((cdata[i] >> 24) & 0xff);
			ret[j++] = (byte) ((cdata[i] >> 16) & 0xff);
			ret[j++] = (byte) ((cdata[i] >> 8) & 0xff);
			ret[j++] = (byte) (cdata[i] & 0xff);
		}
		return ret;
	}

	/**
	 * Hash a password using the OpenBSD bcrypt scheme
	 * @param password the password to hash
	 * @param salt the salt to hash with (perhaps generated using BCrypt.gensalt)
	 * @return the hashed password
	 */
	public static String hashpw(String password, String salt) {
		BCrypt B;
		String real_salt;
		byte passwordb[], saltb[], hashed[];
		char minor = (char) 0;
		int rounds, off = 0;
		StringBuilder rs = new StringBuilder();

		int saltLength = salt.length();

		if (saltLength < 28) {
			throw new IllegalArgumentException("Invalid salt");
		}

		if (salt.charAt(0) != '$' || salt.charAt(1) != '2') {
			throw new IllegalArgumentException("Invalid salt version");
		}
		if (salt.charAt(2) == '$') {
			off = 3;
		}
		else {
			minor = salt.charAt(2);
			if (minor != 'a' || salt.charAt(3) != '$') {
				throw new IllegalArgumentException("Invalid salt revision");
			}
			off = 4;
		}

		if (saltLength - off < 25) {
			throw new IllegalArgumentException("Invalid salt");
		}

		// Extract number of rounds
		if (salt.charAt(off + 2) > '$') {
			throw new IllegalArgumentException("Missing salt rounds");
		}
		rounds = Integer.parseInt(salt.substring(off, off + 2));

		real_salt = salt.substring(off + 3, off + 25);
		try {
			passwordb = (password + (minor >= 'a' ? "\000" : "")).getBytes("UTF-8");
		}
		catch (UnsupportedEncodingException uee) {
			throw new AssertionError("UTF-8 is not supported");
		}

		saltb = decode_base64(real_salt, BCRYPT_SALT_LEN);

		B = new BCrypt();
		hashed = B.crypt_raw(passwordb, saltb, rounds);

		rs.append("$2");
		if (minor >= 'a') {
			rs.append(minor);
		}
		rs.append("$");
		if (rounds < 10) {
			rs.append("0");
		}
		rs.append(rounds);
		rs.append("$");
		encode_base64(saltb, saltb.length, rs);
		encode_base64(hashed, bf_crypt_ciphertext.length * 4 - 1, rs);
		return rs.toString();
	}

	/**
	 * Generate a salt for use with the BCrypt.hashpw() method
	 * @param log_rounds the log2 of the number of rounds of hashing to apply - the work
	 * factor therefore increases as 2**log_rounds. Minimum 4, maximum 31.
	 * @param random an instance of SecureRandom to use
	 * @return an encoded salt value
	 */
	public static String gensalt(int log_rounds, SecureRandom random) {
		if (log_rounds < MIN_LOG_ROUNDS || log_rounds > MAX_LOG_ROUNDS) {
			throw new IllegalArgumentException("Bad number of rounds");
		}
		StringBuilder rs = new StringBuilder();
		byte rnd[] = new byte[BCRYPT_SALT_LEN];

		random.nextBytes(rnd);

		rs.append("$2a$");
		if (log_rounds < 10) {
			rs.append("0");
		}
		rs.append(log_rounds);
		rs.append("$");
		encode_base64(rnd, rnd.length, rs);
		return rs.toString();
	}

	/**
	 * Generate a salt for use with the BCrypt.hashpw() method
	 * @param log_rounds the log2 of the number of rounds of hashing to apply - the work
	 * factor therefore increases as 2**log_rounds. Minimum 4, maximum 31.
	 * @return an encoded salt value
	 */
	public static String gensalt(int log_rounds) {
		return gensalt(log_rounds, new SecureRandom());
	}

	/**
	 * Generate a salt for use with the BCrypt.hashpw() method, selecting a reasonable
	 * default for the number of hashing rounds to apply
	 * @return an encoded salt value
	 */
	public static String gensalt() {
		return gensalt(GENSALT_DEFAULT_LOG2_ROUNDS);
	}

	/**
	 * Check that a plaintext password matches a previously hashed one
	 * @param plaintext the plaintext password to verify
	 * @param hashed the previously-hashed password
	 * @return true if the passwords match, false otherwise
	 */
	public static boolean checkpw(String plaintext, String hashed) {
		return equalsNoEarlyReturn(hashed, hashpw(plaintext, hashed));
	}

	static boolean equalsNoEarlyReturn(String a, String b) {
		char[] caa = a.toCharArray();
		char[] cab = b.toCharArray();

		if (caa.length != cab.length) {
			return false;
		}

		byte ret = 0;
		for (int i = 0; i < caa.length; i++) {
			ret |= caa[i] ^ cab[i];
		}
		return ret == 0;
	}
}


--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/BCryptPasswordEncoder.java
/*
 * Copyright 2002-2011 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.example.application.util.hash.bcrypt;


import com.example.application.util.hash.PasswordEncoder;

import java.security.SecureRandom;
import java.util.logging.Logger;
import java.util.regex.Pattern;

/**
 * Implementation of PasswordEncoder that uses the BCrypt strong hashing function. Clients
 * can optionally supply a "strength" (a.k.a. log rounds in BCrypt) and a SecureRandom
 * instance. The larger the strength parameter the more work will have to be done
 * (exponentially) to hash the passwords. The default value is 10.
 *
 * @author Dave Syer
 *
 */
public class BCryptPasswordEncoder implements PasswordEncoder {
	private Pattern BCRYPT_PATTERN = Pattern
			.compile("\\A\\$2a?\\$\\d\\d\\$[./0-9A-Za-z]{53}");
	private final Logger logger = Logger.getLogger(BCryptPasswordEncoder.class.getSimpleName());

	private final int strength;

	private final SecureRandom random;

	public BCryptPasswordEncoder() {
		this(-1);
	}

	/**
	 * @param strength the log rounds to use, between 4 and 31
	 */
	public BCryptPasswordEncoder(int strength) {
		this(strength, null);
	}

	/**
	 * @param strength the log rounds to use, between 4 and 31
	 * @param random the secure random instance to use
	 *
	 */
	public BCryptPasswordEncoder(int strength, SecureRandom random) {
		if (strength != -1 && (strength < BCrypt.MIN_LOG_ROUNDS || strength > BCrypt.MAX_LOG_ROUNDS)) {
			throw new IllegalArgumentException("Bad strength");
		}
		this.strength = strength;
		this.random = random;
	}

	public String encode(CharSequence rawPassword) {
		String salt;
		if (strength > 0) {
			if (random != null) {
				salt = BCrypt.gensalt(strength, random);
			}
			else {
				salt = BCrypt.gensalt(strength);
			}
		}
		else {
			salt = BCrypt.gensalt();
		}
		return BCrypt.hashpw(rawPassword.toString(), salt);
	}

	public boolean matches(CharSequence rawPassword, String encodedPassword) {
		if (encodedPassword == null || encodedPassword.length() == 0) {
			logger.warning("Empty encoded password");
			return false;
		}

		if (!BCRYPT_PATTERN.matcher(encodedPassword).matches()) {
			logger.warning("Encoded password does not look like BCrypt");
			return false;
		}

		return BCrypt.checkpw(rawPassword.toString(), encodedPassword);
	}
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/bcrypt/package-info.java

/**
 * The BCrypt codes are copied from Spring Security project.
 * Just do some small modifications for our project.
 */
package com.example.application.util.hash.bcrypt;

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/application/util/hash/plain/PlainPasswordEncoder.java
package com.example.application.util.hash.plain;


import com.example.application.util.hash.PasswordEncoder;

/**
 *
 * @author hantsy
 */
public class PlainPasswordEncoder implements PasswordEncoder {

    @Override
    public String encode(CharSequence rawPassword) {
        return rawPassword.toString();
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return rawPassword.equals(encodedPassword);
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AbstractAuditableEntity.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.common;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.AttributeOverride;
import javax.persistence.Column;
import javax.persistence.MappedSuperclass;
import java.time.LocalDateTime;

/**
 *
 * @author hantsy
 * @param <ID>
 */
@MappedSuperclass
@Setter
@Getter
// applied it in orm.xml instead.
//@EntityListeners(AuditEntityListener.class)
public class AbstractAuditableEntity<ID> extends AbstractEntity<ID> {

    private static final long serialVersionUID = 1L;

    @Column(name = "created_at")
    private LocalDateTime createdDate;

    @Column(name = "last_modified_at")
    private LocalDateTime lastModifiedDate;

    @AttributeOverride(name = "username", column = @Column(name = "created_by"))
    private Username createdBy;

    @AttributeOverride(name = "username", column = @Column(name = "last_modified_by"))
    private Username lastModifiedBy;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AbstractEntity.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.common;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@MappedSuperclass
@Getter
@Setter
public class AbstractEntity<ID> implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    private ID id;

    @Version
    @Column(name = "version")
    private Long version;

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/AuditingEntityListener.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.common;

import com.example.infrastructure.security.Authenticated;
import com.example.infrastructure.security.UserInfo;

import javax.enterprise.inject.spi.CDI;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import java.time.LocalDateTime;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author hantsy
 */
public class AuditingEntityListener {

    private static final Logger LOG = Logger.getLogger(AuditingEntityListener.class.getName());

    @PrePersist
    public void beforePersist(Object entity) {
        if (entity instanceof AbstractAuditableEntity) {
            AbstractAuditableEntity o = (AbstractAuditableEntity) entity;
            final LocalDateTime now = LocalDateTime.now();
            o.setCreatedDate(now);
            o.setLastModifiedDate(now);

            if (o.getCreatedBy() == null) {
                o.setCreatedBy(currentUser());
            }
        }
    }

    @PreUpdate
    public void beforeUpdate(Object entity) {
        if (entity instanceof AbstractAuditableEntity) {
            AbstractAuditableEntity o = (AbstractAuditableEntity) entity;
            o.setLastModifiedDate(LocalDateTime.now());

            if (o.getLastModifiedBy() == null) {
                o.setLastModifiedBy(currentUser());
            }
        }
    }

    private Username currentUser() {
        try {
            UserInfo user = CDI.current().select(UserInfo.class, Authenticated.INSTANCE).get();
            LOG.log(Level.INFO, "set username for entity in AuditEntityListener: {0}", user);
            if (user == null) {
                return null;
            }
            return new Username(user.getName());
        } catch (Exception e) {
            return null;
        }

    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/Boolean2StringConverter.java
package com.example.domain.common;

import javax.persistence.AttributeConverter;
import javax.persistence.Converter;

@Converter(autoApply = true)
public class Boolean2StringConverter implements AttributeConverter<Boolean, String> {

    @Override
    public String convertToDatabaseColumn(Boolean attribute) {
        return attribute ? "on" : "off";
    }

    @Override
    public Boolean convertToEntityAttribute(String dbData) {
        return "on".equals(dbData) || Boolean.parseBoolean(dbData) || Boolean.FALSE;
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/common/Username.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.common;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Embeddable;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Embeddable
public class Username implements Serializable {
    
    private String username;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Count.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.task;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Embeddable;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Embeddable
public class Count implements Serializable {

    private long count = 0L;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Existence.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.task;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Embeddable;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Embeddable
public class Existence implements Serializable {

    private boolean existed = false;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/Task.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.task;

import com.example.domain.common.AbstractAuditableEntity;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.function.Function;

import static com.example.domain.task.Task.Status.TODO;

/**
 * @author hantsy
 */
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Task extends AbstractAuditableEntity<Long> {

    private static final long serialVersionUID = 1L;

    public static enum Status {
        TODO, DOING, DONE;
    }

    public static Comparator<Task> COMPARATOR = Comparator
            .comparing(Task::getName)
            .thenComparing(Task::getDescription);

    public static Function<Task, String> TO_STRING = t
            -> "Post["
            + "\n title:" + t.getName()
            + "\n content:" + t.getDescription()
            + "\n status:" + t.getStatus()
            + "\n createdAt:" + t.getCreatedDate()
            + "\n lastModifiedAt:" + t.getLastModifiedDate()
            + "]";


    public static Task of(String name, String description) {
        final Task task = new Task();
        task.setName(name);
        task.setDescription(description);

        return task;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "description")
    private String description;

    @Enumerated(EnumType.STRING)
    @Column(name = "status")
    private Status status = TODO;

    @Column(name = "created_date")
    private LocalDateTime createdDate;

    @Column(name = "last_modified_date")
    private LocalDateTime lastModifiedDate;

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/task/TaskRepository.java
package com.example.domain.task;

import java.util.List;
import java.util.Optional;

public interface TaskRepository {
    long countByKeyword(String keyword, Task.Status status);
    
    List<Task> searchByKeyword(String keyword,
                               Task.Status status,
                               int offset,
                               int limit);
    
    List<Task> findByCreatedBy(String name);
    
    Task save(Task task);
    
    Optional<Task> findOptionalById(Long id);
    
    boolean delete(Task task);
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/user/User.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.domain.user;

import com.example.domain.common.AbstractEntity;
import lombok.*;

import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.FetchType;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import java.util.HashSet;
import java.util.Set;

/**
 * @author hantsy
 */
@Entity
@Table(name = "users")
@Data
@EqualsAndHashCode(callSuper = false)
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class User extends AbstractEntity<Long> {

    @NotBlank
    private String username;
    @NotBlank
    private String password;

    private String firstName;
    private String lastName;

    @Email
    @NotBlank
    private String email;

    // https://stackoverflow.com/questions/22821695/how-to-fix-hibernate-lazyinitializationexception-failed-to-lazily-initialize-a

    // @ElementCollection()
    @ElementCollection(fetch = FetchType.EAGER)
    private Set<String> authorities = new HashSet<>();

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/domain/user/UserRepository.java
package com.example.domain.user;

import java.util.List;
import java.util.Optional;

public interface UserRepository {
    Optional<User> findByUsername(String caller);
    
    Optional<User> findByEmail(String email);
    
    User save(User user);
    
    List<User> findAll();
    
    long countAll();
    
    boolean delete(User user);
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/package-info.java
/**
 *  The infrastructure codes.
 */
package com.example.infrastructure;
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/AbstractRepository.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.persistence.jpa;

import com.example.domain.common.AbstractEntity;

import javax.persistence.EntityManager;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaDelete;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Root;
import java.lang.reflect.ParameterizedType;
import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

/**
 * @param <T>  Entity type.
 * @param <ID> Entity ID type.
 * @author hantsy
 */
public abstract class AbstractRepository<T extends AbstractEntity<ID>, ID> {

    protected abstract EntityManager entityManager();

    private Class<T> entityClass() {
        @SuppressWarnings("unchecked")
        ParameterizedType parameterizedType = (ParameterizedType) this.getClass().getGenericSuperclass();
        return (Class<T>) parameterizedType.getActualTypeArguments()[0];
    }

    public List<T> findAll() {

        CriteriaBuilder cb = this.entityManager().getCriteriaBuilder();

        CriteriaQuery<T> q = cb.createQuery(entityClass());
        Root<T> c = q.from(entityClass());

        return entityManager().createQuery(q).getResultList();
    }

    public T save(T entity) {
        if (entity.getId() == null) {
            entityManager().persist(entity);

            return entity;
        } else {
            return entityManager().merge(entity);
        }
    }

    public T findById(ID id) {
        return entityManager().find(entityClass(), id);
    }

    public boolean delete(T entity) {
        T _entity = entityManager().merge(entity);
        entityManager().remove(_entity);
        return true;
    }

    public int deleteAll() {
        CriteriaBuilder cb = this.entityManager().getCriteriaBuilder();
        CriteriaDelete<T> q = cb.createCriteriaDelete(entityClass());
        return entityManager().createQuery(q).executeUpdate();
    }

    public int deleteById(ID id) {
        CriteriaBuilder cb = this.entityManager().getCriteriaBuilder();
        CriteriaDelete<T> q = cb.createCriteriaDelete(entityClass());
        Root<T> c = q.from(entityClass());
        q.where(cb.equal(c.get("id"), id));
        return entityManager().createQuery(q).executeUpdate();
    }

    public Stream<T> stream() {
        CriteriaBuilder cb = this.entityManager().getCriteriaBuilder();
        CriteriaQuery<T> q = cb.createQuery(entityClass());
        Root<T> c = q.from(entityClass());

        return entityManager().createQuery(q).getResultStream();
    }

    public Optional<T> findOptionalById(ID id) {
        return Optional.ofNullable(findById(id));
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/JpaTaskRepository.java
package com.example.infrastructure.persistence.jpa;

import com.example.domain.task.Task;
import com.example.domain.task.TaskRepository;
import com.example.domain.task.Task_;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * @author hantsy
 */
@Stateless
public class JpaTaskRepository extends AbstractRepository<Task, Long> implements TaskRepository {

    @PersistenceContext
    EntityManager em;

    @Override
    public long countByKeyword(String keyword, Task.Status status) {
        CriteriaBuilder cb = this.em.getCriteriaBuilder();
        CriteriaQuery<Long> q = cb.createQuery(Long.class);
        Root<Task> c = q.from(Task.class);
        List<Predicate> predicates = new ArrayList<>();

        if (keyword != null && !keyword.trim().isEmpty()) {
            predicates.add(
                    cb.or(
                            cb.like(c.get(Task_.name), '%' + keyword + '%'),
                            cb.like(c.get(Task_.description), '%' + keyword + '%')
                    )
            );
        }
        if (status != null) {
            predicates.add(cb.equal(c.get(Task_.status), status));
        }

        q.where(predicates.toArray(new Predicate[0]));
        TypedQuery<Long> query = em.createQuery(q.select(cb.count(c)));

        return query.getSingleResult();
    }

    @Override
    public List<Task> searchByKeyword(String keyword,
                                      Task.Status status,
                                      int offset,
                                      int limit) {
        CriteriaBuilder cb = this.em.getCriteriaBuilder();

        CriteriaQuery<Task> q = cb.createQuery(Task.class);
        Root<Task> c = q.from(Task.class);
        List<Predicate> predicates = new ArrayList<>();

        if (keyword != null && !keyword.trim().isEmpty()) {
            predicates.add(
                    cb.or(
                            cb.like(c.get(Task_.name), '%' + keyword + '%'),
                            cb.like(c.get(Task_.description), '%' + keyword + '%')
                    )
            );
        }
        if (status != null) {
            predicates.add(cb.equal(c.get(Task_.status), status));
        }

        q.where(predicates.toArray(new Predicate[0]));
        TypedQuery<Task> query = em.createQuery(q).setFirstResult(offset).setMaxResults(limit);

        return query.getResultList();
    }

    @Override
    public List<Task> findByCreatedBy(String name) {
        Objects.requireNonNull(name, "username can not be null");
        return this.stream().filter(t -> name.equals(t.getCreatedBy().getUsername())).collect(Collectors.toList());
    }

    @Override
    protected EntityManager entityManager() {
        return this.em;
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/persistence/jpa/JpaUserRepository.java
package com.example.infrastructure.persistence.jpa;


import com.example.domain.user.User;
import com.example.domain.user.UserRepository;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.Objects;
import java.util.Optional;

@Stateless
public class JpaUserRepository extends AbstractRepository<User, Long> implements UserRepository {
    
    @PersistenceContext
    private EntityManager em;
    
    @Override
    protected EntityManager entityManager() {
        return this.em;
    }
    
    @Override
    public Optional<User> findByUsername(String caller) {
        Objects.requireNonNull(caller, "username can not be null");
        return this.stream().filter(u -> u.getUsername().equals(caller)).findFirst();
    }
    
    @Override
    public Optional<User> findByEmail(String email) {
        Objects.requireNonNull(email, "email can not be null");
        return this.stream().filter(u -> u.getEmail().equals(email)).findFirst();
    }
    
    @Override
    public long countAll() {
        return this.stream().count();
    }
    
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/Authenticated.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security;

import javax.enterprise.util.AnnotationLiteral;
import javax.inject.Qualifier;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

/**
 * @author hantsy
 */
@Qualifier
@Retention(RUNTIME)
@Target({METHOD, FIELD, PARAMETER, TYPE})
public @interface Authenticated {
    Literal INSTANCE = new Literal();

    class Literal extends AnnotationLiteral<Authenticated> implements Authenticated {
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/AuthenticatedUserInfoProducer.java
package com.example.infrastructure.security;

import javax.enterprise.context.RequestScoped;
import javax.enterprise.event.Observes;
import javax.enterprise.inject.Produces;
import javax.inject.Inject;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author hantsy
 */
@RequestScoped
public class AuthenticatedUserInfoProducer {

    @Inject
    Logger LOG;

    private UserInfo currentUser;

    @Produces
    @Authenticated
    public UserInfo getUserInfo() {
        return this.currentUser;
    }

    public void handleAuthenticationEvent(@Observes @Authenticated UserInfo authenticatedUser) {
        LOG.log(Level.INFO, "handling authentication event:{0}", authenticatedUser);
        this.currentUser = authenticatedUser;
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/SecurityConstant.java

package com.example.infrastructure.security;

/**
 *
 * @author hantsy
 */
public class SecurityConstant {

    private SecurityConstant() {
    }

    // two roles will be used in this application.
    public static final String ROLE_USER = "ROLE_USER";
    public static final String ROLE_ADMIN = "ROLE_ADMIN";

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/UserInfo.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.HashSet;
import java.util.Set;

import static java.util.Arrays.asList;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class UserInfo {

    private String name;
    private Set<String> roles = new HashSet<>();

    public boolean hasRole(String _role) {
        return this.roles.contains(_role);
    }

    public boolean hasAnyRoles(String... _roles) {
        return this.roles.stream().anyMatch(c -> asList(_roles).contains(c));
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JpaIdentityStore.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security.jwt;


import com.example.domain.user.UserRepository;
import com.example.application.util.hash.Crypto;
import com.example.application.util.hash.PasswordEncoder;

import javax.annotation.PostConstruct;
import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import javax.security.enterprise.credential.Credential;
import javax.security.enterprise.credential.UsernamePasswordCredential;
import javax.security.enterprise.identitystore.CredentialValidationResult;
import javax.security.enterprise.identitystore.IdentityStore;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

import static javax.security.enterprise.identitystore.CredentialValidationResult.INVALID_RESULT;
import static javax.security.enterprise.identitystore.CredentialValidationResult.NOT_VALIDATED_RESULT;

/**
 *
 * @author hantsy
 */
@RequestScoped
public class JpaIdentityStore implements IdentityStore {

    @Inject
    private Logger LOG;

    @Inject
    private UserRepository users;

    @Inject
    @Crypto(Crypto.Type.BCRYPT)
    private PasswordEncoder passwordHash;

    @PostConstruct
    public void init() {
        LOG.log(Level.INFO, "initializing JpaIdentityStore...");
    }

    @Override
    public CredentialValidationResult validate(Credential credential) {
        CredentialValidationResult result;

        if (credential instanceof UsernamePasswordCredential) {
            UsernamePasswordCredential usernamePassword = (UsernamePasswordCredential) credential;

            result = users.findByUsername(usernamePassword.getCaller())
                .map(
                    u -> passwordHash.matches(new String(usernamePassword.getPassword().getValue()), u.getPassword())
                    ? new CredentialValidationResult(usernamePassword.getCaller(), u.getAuthorities())
                    : INVALID_RESULT
                )
                .orElse(INVALID_RESULT);

        } else {
            result = NOT_VALIDATED_RESULT;
        }
        return result;
    }

    @Override
    public Set<String> getCallerGroups(CredentialValidationResult validationResult) {
//        return users.findByUsername(validationResult.getCallerPrincipal().getName())
//                .map(user -> user.getAuthorities())
//                .orElse(emptySet());
        return validationResult.getCallerGroups();

    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtAuthenticationMechanism.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security.jwt;

import com.example.infrastructure.security.Authenticated;
import com.example.infrastructure.security.UserInfo;
import io.jsonwebtoken.ExpiredJwtException;

import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.event.Event;
import javax.inject.Inject;
import javax.security.enterprise.AuthenticationStatus;
import javax.security.enterprise.authentication.mechanism.http.HttpAuthenticationMechanism;
import javax.security.enterprise.authentication.mechanism.http.HttpMessageContext;
import javax.security.enterprise.authentication.mechanism.http.RememberMe;
import javax.security.enterprise.credential.UsernamePasswordCredential;
import javax.security.enterprise.identitystore.CredentialValidationResult;
import javax.security.enterprise.identitystore.IdentityStoreHandler;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.core.HttpHeaders;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author hantsy
 */
@RememberMe(
        cookieMaxAgeSecondsExpression ="jwtProperties.remembermeValidityInSeconds" ,
        isRememberMeExpression = "self.isRememberMe(httpMessageContext)"
)
@ApplicationScoped
public class JwtAuthenticationMechanism implements HttpAuthenticationMechanism {
    public static final String AUTHORIZATION_PREFIX = "Bearer ";

    @Inject
    Logger LOGGER;

    /**
     * Access to the IdentityStore(AuthenticationIdentityStore,AuthorizationIdentityStore) is abstracted by the
     * IdentityStoreHandler to allow for multiple identity stores to logically act as a single IdentityStore
     */
    @Inject
    private IdentityStoreHandler identityStoreHandler;

    @Inject
    private TokenProvider tokenProvider;

    @Inject
    @Authenticated
    private Event<UserInfo> authenticatedEvent;

    @Override
    public AuthenticationStatus validateRequest(HttpServletRequest request, HttpServletResponse response, HttpMessageContext context) {

        LOGGER.log(Level.INFO, "validateRequest: {0}, {1}", new Object[]{request.getRequestURI(), request.getMethod()});
        // Get the (caller) name and password from the request
        // NOTE: This is for the smallest possible example only. In practice
        // putting the password in a request query parameter is highly insecure
        String name = request.getParameter("username");
        String password = request.getParameter("password");
        String token = extractToken(context);

        if (name != null && password != null
                && "POST".equals(request.getMethod())
                && request.getRequestURI().endsWith("/auth/login")) {
            LOGGER.log(Level.INFO, "user credentials : {0}, {1}", new String[]{name, password});
            // validation of the credential using the identity store
            CredentialValidationResult result = identityStoreHandler.validate(new UsernamePasswordCredential(name, password));
            if (result.getStatus() == CredentialValidationResult.Status.VALID) {
                // Communicate the details of the authenticated user to the container and return SUCCESS.
                return createToken(result, context);
            }
            // if the authentication failed, we return the unauthorized status in the http response
            return context.responseUnauthorized();
        } else if (token != null) {
            // validation of the jwt credential
            return validateToken(token, context);
        } else if (context.isProtected()) {
            // A protected resource is a resource for which a constraint has been defined.
            // if there are no credentials and the resource is protected, we response with unauthorized status
            return context.responseUnauthorized();
        }
        // there are no credentials AND the resource is not protected, 
        // SO Instructs the container to "do nothing"
        return context.doNothing();
    }

    /**
     * To validate the JWT token e.g Signature check, JWT claims check(expiration) etc
     *
     * @param token   The JWT access tokens
     * @param context
     * @return the AuthenticationStatus to notify the container
     */
    private AuthenticationStatus validateToken(String token, HttpMessageContext context) {
        try {
            if (tokenProvider.validateToken(token)) {
                JwtCredential credential = tokenProvider.getCredential(token);

                //fire an @Authenticated CDI event.
                authenticatedEvent.fire(new UserInfo(credential.getPrincipal(), credential.getAuthorities()));

                return context.notifyContainerAboutLogin(credential.getPrincipal(), credential.getAuthorities());
            }
            // if token invalid, response with unauthorized status
            return context.responseUnauthorized();
        } catch (ExpiredJwtException eje) {
            LOGGER.log(Level.INFO, "Security exception for user {0} - {1}", new String[]{eje.getClaims().getSubject(), eje.getMessage()});
            return context.responseUnauthorized();
        }
    }

    /**
     * Create the JWT using CredentialValidationResult received from IdentityStoreHandler
     *
     * @param result  the result from validation of UsernamePasswordCredential
     * @param context
     * @return the AuthenticationStatus to notify the container
     */
    private AuthenticationStatus createToken(CredentialValidationResult result, HttpMessageContext context) {
        if (!isRememberMe(context)) {
            String jwt = tokenProvider.createToken(result.getCallerPrincipal().getName(), result.getCallerGroups(), false);
            context.getResponse().setHeader(HttpHeaders.AUTHORIZATION, AUTHORIZATION_PREFIX + jwt);
        }

        //fire an @Authenticated CDI event.
        authenticatedEvent.fire(new UserInfo(result.getCallerPrincipal().getName(), result.getCallerGroups()));

        return context.notifyContainerAboutLogin(result.getCallerPrincipal(), result.getCallerGroups());
    }

    /**
     * To extract the JWT from Authorization HTTP header
     *
     * @param context
     * @return The JWT access tokens
     */
    private String extractToken(HttpMessageContext context) {
        String authorizationHeader = context.getRequest().getHeader(HttpHeaders.AUTHORIZATION);
        if (authorizationHeader != null && authorizationHeader.startsWith(AUTHORIZATION_PREFIX)) {
            String token = authorizationHeader.substring(AUTHORIZATION_PREFIX.length());
            return token;
        }
        return null;
    }

    /**
     * this function invoked using RememberMe.isRememberMeExpression EL expression
     *
     * @param context
     * @return The remember me flag
     */
    public Boolean isRememberMe(HttpMessageContext context) {
        return Boolean.valueOf(context.getRequest().getParameter("rememberMe"));
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtCredential.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security.jwt;

import javax.security.enterprise.credential.Credential;
import java.util.Set;

/**
 *
 * @author hantsy
 */
public class JwtCredential implements Credential {

    private final String principal;
    private final Set<String> authorities;

    public JwtCredential(String principal, Set<String> authorities) {
        this.principal = principal;
        this.authorities = authorities;
    }

    public String getPrincipal() {
        return principal;
    }

    public Set<String> getAuthorities() {
        return authorities;
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtProperties.java
package com.example.infrastructure.security.jwt;

import lombok.Getter;
import org.eclipse.microprofile.config.inject.ConfigProperty;

import javax.annotation.PostConstruct;
import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.inject.Named;
import java.util.logging.Level;
import java.util.logging.Logger;

@ApplicationScoped
@Named("jwtProperties")
@Getter
public class JwtProperties {
    private static final Logger LOGGER = Logger.getLogger(JwtProperties.class.getName());

    @Inject
    @ConfigProperty(name = "jwt.secretKey", defaultValue = "rzxlszyykpbgqcflzxsqcysyhljt")
    private String secretKey;

    @Inject
    @ConfigProperty(name = "jwt.tokenValidityInSeconds", defaultValue = "3600")
    private int tokenValidityInSeconds;

    @Inject
    @ConfigProperty(name = "jwt.remembermeValidityInSeconds")
    private int remembermeValidityInSeconds;

    @PostConstruct
    public void init() {
        LOGGER.log(Level.INFO,
                "Configured jwt properties: secretKey={0}, tokenValidityInSeconds={1}, remembermeValidityInSeconds={2}",
                new Object[]{secretKey, tokenValidityInSeconds, remembermeValidityInSeconds});
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/JwtRememberMeIdentityStore.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security.jwt;

import io.jsonwebtoken.ExpiredJwtException;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.security.enterprise.CallerPrincipal;
import javax.security.enterprise.credential.RememberMeCredential;
import javax.security.enterprise.identitystore.CredentialValidationResult;
import javax.security.enterprise.identitystore.RememberMeIdentityStore;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

import static javax.security.enterprise.identitystore.CredentialValidationResult.INVALID_RESULT;

/**
 *
 * @author hantsy
 */
@ApplicationScoped
public class JwtRememberMeIdentityStore implements RememberMeIdentityStore {

    @Inject
    private Logger LOGGER ;

    @Inject
    private TokenProvider tokenProvider;

    @Override
    public CredentialValidationResult validate(RememberMeCredential rememberMeCredential) {
        try {
            if (tokenProvider.validateToken(rememberMeCredential.getToken())) {
                JwtCredential credential = tokenProvider.getCredential(rememberMeCredential.getToken());
                return new CredentialValidationResult(credential.getPrincipal(), credential.getAuthorities());
            }
            // if token invalid, response with invalid result status
            return INVALID_RESULT;
        } catch (ExpiredJwtException eje) {
            LOGGER.log(Level.INFO, "Security exception for user {0} - {1}", new Object[]{eje.getClaims().getSubject(), eje.getMessage()});
            return INVALID_RESULT;
        }
    }

    @Override
    public String generateLoginToken(CallerPrincipal callerPrincipal, Set<String> groups) {
        return tokenProvider.createToken(callerPrincipal.getName(), groups, true);
    }

    @Override
    public void removeLoginToken(String token) {
        // Stateless authentication means at server side we don't maintain the state
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/package-info.java
/**
 *  The JWT authentication implementation is based on:
 *  https://github.com/javaee-samples/javaee8-samples
 * 
 * <ul>
 *  <li> Replace the dummy IdentityStore with JPA backend IdentityStore.
 *  <li> When the authentication is successful, fire an @Anthenticated CDI event. 
 * </ul>
 */
package com.example.infrastructure.security.jwt;

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/infrastructure/security/jwt/TokenProvider.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.infrastructure.security.jwt;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;

import javax.annotation.PostConstruct;
import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import java.security.Key;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.joining;

/**
 * @author hantsy
 */
@ApplicationScoped
public class TokenProvider {

    @Inject
    Logger LOGGER;

    @Inject
    JwtProperties properties;

    private static final String AUTHORITIES_KEY = "auth";

    private Key secretKey;

    private long tokenValidity;

    private long tokenValidityForRememberMe;

    @PostConstruct
    public void init() {
        byte[] secret = Base64.getEncoder().encode(properties.getSecretKey().getBytes());
        this.secretKey = Keys.hmacShaKeyFor(secret);
        this.tokenValidity = TimeUnit.SECONDS.toMillis(properties.getTokenValidityInSeconds());
        this.tokenValidityForRememberMe = TimeUnit.SECONDS.toMillis(properties.getRemembermeValidityInSeconds());
    }

    public String createToken(String username, Set<String> authorities, Boolean rememberMe) {
        Date now = new Date();
        long validity = rememberMe ? tokenValidityForRememberMe : tokenValidity;
        Date expiration = new Date(now.getTime() + validity);

        Claims claims = Jwts.claims().setSubject(username);
        if (!authorities.isEmpty()) {
            claims.put(AUTHORITIES_KEY, authorities.stream().collect(joining(",")));
        }

        return Jwts.builder()
                .setClaims(claims)
                .signWith(this.secretKey, SignatureAlgorithm.HS512)
                .setIssuedAt(now)
                .setExpiration(expiration)
                .compact();
    }

    public JwtCredential getCredential(String token) {
        Claims claims = Jwts.parserBuilder().setSigningKey(secretKey).build()
                .parseClaimsJws(token)
                .getBody();

        Set<String> authorities
                = claims.get(AUTHORITIES_KEY) == null ?
                Collections.emptySet()
                : Arrays.stream(claims.get(AUTHORITIES_KEY).toString().split(",")).collect(Collectors.toSet());

        return new JwtCredential(claims.getSubject(), authorities);
    }

    public boolean validateToken(String authToken) {
        try {
            Jwts.parserBuilder().setSigningKey(secretKey).build().parse(authToken);
            return true;
        } catch (SecurityException e) {
            LOGGER.log(Level.INFO, "Invalid JWT signature: {0}", e.getMessage());
            return false;
        }
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/RestConfiguration.java
package com.example.interfaces;

import javax.annotation.security.DeclareRoles;
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;

import static com.example.infrastructure.security.SecurityConstant.ROLE_ADMIN;
import static com.example.infrastructure.security.SecurityConstant.ROLE_USER;

@DeclareRoles({ROLE_USER, ROLE_ADMIN})
@ApplicationPath("api")
public class RestConfiguration extends Application {

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/auth/AuthResource.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.auth;

import com.example.infrastructure.security.Authenticated;
import com.example.infrastructure.security.UserInfo;

import javax.inject.Inject;
import javax.json.Json;
import javax.json.JsonObject;
import javax.security.enterprise.SecurityContext;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.logging.Level;
import java.util.logging.Logger;

import static javax.ws.rs.core.Response.Status.UNAUTHORIZED;
import static javax.ws.rs.core.Response.ok;
import static javax.ws.rs.core.Response.status;

/**
 *
 * @author hantsy
 */
@Path("auth")
public class AuthResource {

    @Inject
    Logger LOGGER;

    @Inject
    private SecurityContext securityContext;

    @Inject
    @Authenticated
    UserInfo userInfo;

    @POST
    @Path("login")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public Response login() {
        LOGGER.log(Level.INFO, "login");
        if (securityContext.getCallerPrincipal() != null) {
            JsonObject result = Json.createObjectBuilder()
                .add("user", securityContext.getCallerPrincipal().getName())
                .build();
            return ok(result).build();
        }
        return status(UNAUTHORIZED).build();
    }

    @GET
    @Path("userinfo")
    public Response userInfo() {
        LOGGER.log(Level.INFO, "user info:{0}", userInfo);
        if (securityContext.getCallerPrincipal() != null) {
            return ok(userInfo).build();
        }
        return status(UNAUTHORIZED).build();
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PagedResult.java
package com.example.interfaces.common;

import lombok.Data;

import java.util.List;

@Data
public class PagedResult<T> {
    private List<T> content;
    private long count;

    public PagedResult()  {
    }

    public static <T> PagedResult<T> of(List<T> content, long count) {
        PagedResult<T> result = new PagedResult<>();
        result.setContent(content);
        result.setCount(count);
        return result;
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PageParam.java
package com.example.interfaces.common;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.Value;

import javax.ws.rs.DefaultValue;
import javax.ws.rs.QueryParam;

@Data
@NoArgsConstructor
@AllArgsConstructor(staticName = "of")
public class PageParam {
    @QueryParam("offset")
    @DefaultValue("0")
    private int offset;

    @QueryParam("limit")
    @DefaultValue("10")
    private int limit;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/PrimitiveConverterProvider.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.common;

import java.lang.annotation.Annotation;
import java.lang.reflect.Type;
import javax.ws.rs.ext.ParamConverter;
import javax.ws.rs.ext.ParamConverterProvider;
import javax.ws.rs.ext.Provider;

@Provider
public class PrimitiveConverterProvider implements ParamConverterProvider {

    @Override
    public <T> ParamConverter<T> getConverter(Class<T> rawType, Type genericType, Annotation[] annotations) {

        if (rawType.getName().equals(boolean.class.getName())) {

            return new ParamConverter<T>() {
                @Override
                public T fromString(String value) {
                    return (T) Boolean.valueOf(value != null && value.equals("on"));
                }

                @Override
                public String toString(T value) {
                    return ((Boolean) value) ? "on" : "";
                }
            };

        } else if (rawType.getName().equals(int.class.getName())) {

            return new ParamConverter<T>() {
                @Override
                public T fromString(String value) {

                    try {
                        return (T) (Integer) Integer.parseInt(value);
                    } catch (NumberFormatException e) {
                    }

                    return (T) (Integer) 0;
                }

                @Override
                public String toString(T value) {
                    return "" + value;
                }
            };

        } else {
            return null;
        }
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsFeature.java
package com.example.interfaces.common.cors;

import javax.ws.rs.core.Feature;
import javax.ws.rs.core.FeatureContext;
import javax.ws.rs.ext.Provider;
import java.util.Set;

/**
 * Activate CorsFilter.
 */
@Provider
public class CorsFeature implements Feature {

    @Override
    public boolean configure(FeatureContext context) {
        CorsFilter corsFilter = new CorsFilter();
        corsFilter.getAllowedOrigins().addAll(Set.of("http://localhost:4200"));
        context.register(corsFilter);
        return true;
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsFilter.java
package com.example.interfaces.common.cors;

import javax.ws.rs.ForbiddenException;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.container.ContainerResponseContext;
import javax.ws.rs.container.ContainerResponseFilter;
import javax.ws.rs.container.PreMatching;
import javax.ws.rs.core.Response;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

/**
 * Handles CORS requests both preflight and simple CORS requests.
 * You must bind this as a singleton and set up allowedOrigins and other settings to use.
 *
 * @author <a href="mailto:bill@burkecentral.com">Bill Burke</a>
 * @version $Revision: 1 $
 */
@PreMatching
public class CorsFilter implements ContainerRequestFilter, ContainerResponseFilter
{
    protected boolean allowCredentials = true;
    protected String allowedMethods;
    protected String allowedHeaders;
    protected String exposedHeaders;
    protected int corsMaxAge = -1;
    protected Set<String> allowedOrigins = new HashSet<String>();

    /**
     * Put "*" if you want to accept all origins.
     *
     * @return allowed origins
     */
    public Set<String> getAllowedOrigins()
    {
        return allowedOrigins;
    }

    /**
     * Defaults to true.
     *
     * @return allow credentials
     */
    public boolean isAllowCredentials()
    {
        return allowCredentials;
    }

    public void setAllowCredentials(boolean allowCredentials)
    {
        this.allowCredentials = allowCredentials;
    }

    /**
     * Will allow all by default.
     *
     * @return allowed methods
     */
    public String getAllowedMethods()
    {
        return allowedMethods;
    }

    /**
     * Will allow all by default
     * comma delimited string for Access-Control-Allow-Methods.
     *
     * @param allowedMethods allowed methods
     */
    public void setAllowedMethods(String allowedMethods)
    {
        this.allowedMethods = allowedMethods;
    }

    public String getAllowedHeaders()
    {
        return allowedHeaders;
    }

    /**
     * Will allow all by default
     * comma delimited string for Access-Control-Allow-Headers.
     *
     * @param allowedHeaders allowed headers
     */
    public void setAllowedHeaders(String allowedHeaders)
    {
        this.allowedHeaders = allowedHeaders;
    }

    public int getCorsMaxAge()
    {
        return corsMaxAge;
    }

    public void setCorsMaxAge(int corsMaxAge)
    {
        this.corsMaxAge = corsMaxAge;
    }

    public String getExposedHeaders()
    {
        return exposedHeaders;
    }

    /**
     * Comma delimited list.
     *
     * @param exposedHeaders exposed headers
     */
    public void setExposedHeaders(String exposedHeaders)
    {
        this.exposedHeaders = exposedHeaders;
    }

    @Override
    public void filter(ContainerRequestContext requestContext) throws IOException
    {
        String origin = requestContext.getHeaderString(CorsHeaders.ORIGIN);
        if (origin == null)
        {
            return;
        }
        if (requestContext.getMethod().equalsIgnoreCase("OPTIONS"))
        {
            preflight(origin, requestContext);
        }
        else
        {
            checkOrigin(requestContext, origin);
        }
    }

    @Override
    public void filter(ContainerRequestContext requestContext, ContainerResponseContext responseContext) throws IOException
    {
        String origin = requestContext.getHeaderString(CorsHeaders.ORIGIN);
        if (origin == null || requestContext.getMethod().equalsIgnoreCase("OPTIONS") || requestContext.getProperty("cors.failure") != null)
        {
            // don't do anything if origin is null, its an OPTIONS request, or cors.failure is set
            return;
        }
        responseContext.getHeaders().putSingle(CorsHeaders.ACCESS_CONTROL_ALLOW_ORIGIN, origin);
        responseContext.getHeaders().putSingle(CorsHeaders.VARY, CorsHeaders.ORIGIN);
        if (allowCredentials) responseContext.getHeaders().putSingle(CorsHeaders.ACCESS_CONTROL_ALLOW_CREDENTIALS, "true");

        if (exposedHeaders != null) {
            responseContext.getHeaders().putSingle(CorsHeaders.ACCESS_CONTROL_EXPOSE_HEADERS, exposedHeaders);
        }
    }


    protected void preflight(String origin, ContainerRequestContext requestContext) throws IOException
    {
        checkOrigin(requestContext, origin);

        Response.ResponseBuilder builder = Response.ok();
        builder.header(CorsHeaders.ACCESS_CONTROL_ALLOW_ORIGIN, origin);
        builder.header(CorsHeaders.VARY, CorsHeaders.ORIGIN);
        if (allowCredentials) builder.header(CorsHeaders.ACCESS_CONTROL_ALLOW_CREDENTIALS, "true");
        String requestMethods = requestContext.getHeaderString(CorsHeaders.ACCESS_CONTROL_REQUEST_METHOD);
        if (requestMethods != null)
        {
            if (allowedMethods != null)
            {
                requestMethods = this.allowedMethods;
            }
            builder.header(CorsHeaders.ACCESS_CONTROL_ALLOW_METHODS, requestMethods);
        }
        String allowHeaders = requestContext.getHeaderString(CorsHeaders.ACCESS_CONTROL_REQUEST_HEADERS);
        if (allowHeaders != null)
        {
            if (allowedHeaders != null)
            {
                allowHeaders = this.allowedHeaders;
            }
            builder.header(CorsHeaders.ACCESS_CONTROL_ALLOW_HEADERS, allowHeaders);
        }
        if (corsMaxAge > -1)
        {
            builder.header(CorsHeaders.ACCESS_CONTROL_MAX_AGE, corsMaxAge);
        }
        requestContext.abortWith(builder.build());

    }

    protected void checkOrigin(ContainerRequestContext requestContext, String origin)
    {
        if (!allowedOrigins.contains("*") && !allowedOrigins.contains(origin))
        {
            requestContext.setProperty("cors.failure", true);
            throw new ForbiddenException("Origin: "+ origin+ " is not allowed");
        }
    }
}
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/CorsHeaders.java
package com.example.interfaces.common.cors;

public class CorsHeaders
{
    public static final String ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin";
    public static final String ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials";
    public static final String ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods";
    public static final String ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers";
    public static final String ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age";
    public static final String ORIGIN = "Origin";
    public static final String ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method";
    public static final String ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers";
    public static final String ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers";
    public static final String VARY = "Vary";
}
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/cors/package-info.java
/**
 *  The `CorsFilter` is copied from Resteasy and do some small modifications.
 *
 *  Use the restesy built-in one instead if you are using Resteasy.
 */
package com.example.interfaces.common.cors;
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/common/exceptionMapper/ConstraintViolationExceptionMapper.java
package com.example.interfaces.common.exceptionMapper;

import javax.validation.ConstraintViolationException;
import javax.validation.Path;
import javax.ws.rs.core.Response;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import static javax.ws.rs.core.Response.status;

@Provider
public class ConstraintViolationExceptionMapper implements ExceptionMapper<ConstraintViolationException> {

    @Override
    public Response toResponse(ConstraintViolationException exception) {
        Map<String, String> errors = new HashMap<>();
        exception.getConstraintViolations()
                .forEach(v -> errors.put(lastFieldName(v.getPropertyPath().iterator()), v.getMessage()));
        return status(Response.Status.BAD_REQUEST).entity(errors).build();
    }

    private String lastFieldName(Iterator<Path.Node> nodes) {
        Path.Node last = null;
        while (nodes.hasNext()) {
            last = nodes.next();
        }
        return last.getName();
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/profile/CurrentUserResource.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.profile;

import com.example.domain.task.Task;
import com.example.domain.task.TaskRepository;
import com.example.domain.user.UserRepository;

import javax.ejb.Stateless;
import javax.inject.Inject;
import javax.security.enterprise.SecurityContext;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.container.ResourceContext;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;
import java.util.List;

import static javax.ws.rs.core.Response.Status.*;
import static javax.ws.rs.core.Response.ok;
import static javax.ws.rs.core.Response.status;

/**
 * @author hantsy
 */
@Path("user")
@Stateless
public class CurrentUserResource {

    @Context
    UriInfo uriInfo;

    @Inject
    UserRepository users;

    @Inject
    TaskRepository tasks;

    @Context
    ResourceContext resourceContext;

    @Inject
    SecurityContext securityContext;

    @GET
    @Path("profile")
    public Response user() {
        return users.findByUsername(securityContext.getCallerPrincipal().getName())
                .map(p -> ok(p).build())
                .orElse(status(NOT_FOUND).build());
    }

    @GET
    @Path("posts")
    public Response posts() {
        List<Task> tasksByCreatedBy = tasks.findByCreatedBy(securityContext.getCallerPrincipal().getName());
        return ok(tasksByCreatedBy).build();
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskForm.java
package com.example.interfaces.task;

import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import java.io.Serializable;

@Data
public class TaskForm implements Serializable {

    private static final long serialVersionUID = 1L;

    @NotBlank
    private String name;

    @NotBlank
    @Size(min = 10, max = 2000)
    private String description;


}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskNotFoundException.java
package com.example.interfaces.task;

public class TaskNotFoundException extends RuntimeException {

    public TaskNotFoundException(Long postId) {
        super(String.format("post id:%s not found!", postId));
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskNotFoundExceptionMapper.java
package com.example.interfaces.task;

import javax.inject.Inject;
import javax.ws.rs.core.Response;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author hantsy
 */
@Provider
public class TaskNotFoundExceptionMapper implements ExceptionMapper<TaskNotFoundException> {

    @Inject
    Logger log;

    @Override
    public Response toResponse(TaskNotFoundException exception) {
        log.log(Level.INFO, "handling exception : PostNotFoundException");

        return Response.status(Response.Status.NOT_FOUND)
                .header("Content-Type", "application/json")
                .entity(exception.getMessage())
                .build();
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskResource.java
package com.example.interfaces.task;

import com.example.domain.task.Task;
import com.example.domain.task.TaskRepository;

import javax.annotation.PostConstruct;
import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import javax.validation.Valid;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.logging.Level;
import java.util.logging.Logger;

import static javax.ws.rs.core.Response.*;

@RequestScoped
public class TaskResource {

    @Inject
    Logger log;

    @PathParam("id")
    Long id;

    @Inject
    TaskRepository taskRepository;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response taskDetails() {
        log.log(Level.INFO, "get task by id@{0}", id);

        return taskRepository.findOptionalById(id)
                .map(data -> ok(data).build())
                .orElseThrow(() -> new TaskNotFoundException(id));
    }

    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public Response update(@Valid TaskForm form) {
        log.log(Level.INFO, "updating existed task@id:{0}, form data:{1}", new Object[]{id, form});

        return taskRepository.findOptionalById(id)
                .map(data -> {
                    data.setName(form.getName());
                    data.setDescription(form.getDescription());

                    taskRepository.save(data);
                    return noContent().build();
                })
                .orElseThrow(() -> new TaskNotFoundException(id));
    }

    @PUT
    @Path("status")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response updateStatus(@Valid UpdateStatusRequest status) {
        log.log(Level.INFO, "updating status of the existed task@id:{0}, status:{1}", new Object[]{id, status});

        Task.Status taskStatus = null;
        try {
            taskStatus = Task.Status.valueOf(status.getStatus());
        } catch (Exception e) {
            log.log(Level.SEVERE, "can not parse task status value:{}", status);
            taskStatus = null;
        }

        Task.Status finalTaskStatus = taskStatus;
        return taskRepository.findOptionalById(id)
                .map(data -> {
                    data.setStatus(finalTaskStatus);
                    taskRepository.save(data);
                    return noContent().build();
                })
                .orElseThrow(() -> new TaskNotFoundException(id));
    }

    @DELETE
    public Response delete() {
        log.log(Level.INFO, "deleting task @{0}", id);

        return taskRepository.findOptionalById(id)
                .map(data -> {
                    taskRepository.delete(data);
                    return noContent().build();
                })
                .orElseThrow(() -> new TaskNotFoundException(id));
    }

    @PostConstruct
    private void init() {
        log.config(() -> this.getClass().getSimpleName() + " created");
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/TaskResources.java
package com.example.interfaces.task;

import com.example.domain.task.TaskRepository;
import com.example.interfaces.common.PageParam;
import com.example.domain.task.Task;
import com.example.interfaces.common.PagedResult;

import javax.annotation.PostConstruct;
import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import javax.validation.Valid;
import javax.ws.rs.*;
import javax.ws.rs.container.ResourceContext;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import static javax.ws.rs.core.Response.*;

@Path("tasks")
@RequestScoped
public class TaskResources {

    @Inject
    Logger log;

    @Inject
    TaskRepository taskRepository;

    @Context
    ResourceContext resourceContext;

    @Context
    UriInfo uriInfo;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response allTasks(
            @QueryParam("q") String keyword,
            @QueryParam("status") String status,
            @BeanParam PageParam page
    ) {
        log.log(Level.INFO, "fetching all tasks, keyword: {0} status:{1}", new Object[]{keyword, status});

        Task.Status taskStatus;
        try {
            taskStatus = Task.Status.valueOf(status);
        } catch (Exception e) {
            log.log(Level.SEVERE, "can not parse task status value:{0}", status);
            taskStatus = null;
        }

        List<Task> tasks = taskRepository.searchByKeyword(keyword, taskStatus, page.getOffset(), page.getLimit());
        long count = taskRepository.countByKeyword(keyword, taskStatus);
        return ok(PagedResult.of(tasks, count)).build();
    }


    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response save(@Valid TaskForm form) {
        log.log(Level.INFO, "saving new task @{0}", form);

        Task task = new Task();
        task.setName(form.getName());
        task.setDescription(form.getDescription());

        Task saved = taskRepository.save(task);

        return created(uriInfo.getBaseUriBuilder().path("/tasks/{id}").build(saved.getId())).build();
    }

    @Path("{id}")
    public TaskResource taskResource() {
        return resourceContext.getResource(TaskResource.class);
    }


    @PostConstruct
    private void init() {
        log.config(() -> this.getClass().getSimpleName() + " created");
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/task/UpdateStatusRequest.java
package com.example.interfaces.task;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.validation.constraints.NotBlank;

@Data
@NoArgsConstructor
@AllArgsConstructor(staticName = "of")
public class UpdateStatusRequest {
    @NotBlank
    private String status;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/EmailWasTakenException.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

/**
 *
 * @author hantsy
 */
public class EmailWasTakenException extends RuntimeException {

    public EmailWasTakenException(String email) {
        super(email + " was already taken by others");
    }
    
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/EmailWasTakenExceptionMapper.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

import javax.ws.rs.core.Response;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

/**
 *
 * @author hantsy
 */
@Provider
public class EmailWasTakenExceptionMapper implements ExceptionMapper<EmailWasTakenException> {

    @Override
    public Response toResponse(EmailWasTakenException exception) {
        return Response.status(Response.Status.CONFLICT)
            .entity(exception.getMessage())
            .build();
    }

}
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/RegisterForm.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class RegisterForm implements Serializable {

    @NotBlank
    private String username;

    @NotBlank
    private String password;

    @NotBlank
    private String firstName;

    @NotBlank
    private String lastName;

    @Email
    @NotBlank
    private String email;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserForm.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import java.io.Serializable;

/**
 *
 * @author hantsy
 */
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class UserForm implements Serializable{
     
    @NotBlank
    private String firstName;
    
    @NotBlank
    private String lastName;

    @Email
    @NotBlank
    private String email;
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserMessageBodyWiter.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;


import com.example.domain.user.User;

import javax.json.bind.JsonbBuilder;
import javax.json.bind.JsonbConfig;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.MultivaluedMap;
import javax.ws.rs.ext.MessageBodyWriter;
import javax.ws.rs.ext.Provider;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.annotation.Annotation;
import java.lang.reflect.Type;

/**
 * @author hantsy
 */
@Provider
public class UserMessageBodyWiter implements MessageBodyWriter<User> {

    @Override
    public boolean isWriteable(Class<?> type, Type genericType, Annotation[] annotations, MediaType mediaType) {
        return type == User.class;
    }

    @Override
    public void writeTo(User t, Class<?> type, Type genericType, Annotation[] annotations, MediaType mediaType, MultivaluedMap<String, Object> httpHeaders, OutputStream entityStream) throws IOException, WebApplicationException {
        t.setPassword(null);
        JsonbConfig config = new JsonbConfig().withNullValues(false);
        JsonbBuilder.create(config).toJson(t, entityStream);
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsernameWasTakenException.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

/**
 *
 * @author hantsy
 */
public class UsernameWasTakenException extends RuntimeException {

    public UsernameWasTakenException(String username) {
        super(username + " was already taken by others");
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsernameWasTakenExceptionMapper.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;

import javax.ws.rs.core.Response;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

/**
 *
 * @author hantsy
 */
@Provider
public class UsernameWasTakenExceptionMapper implements ExceptionMapper<UsernameWasTakenException> {

    @Override
    public Response toResponse(UsernameWasTakenException exception) {
        return Response.status(Response.Status.CONFLICT)
            .entity(exception.getMessage())
            .build();
    }

}
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UserResource.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;


import com.example.domain.user.UserRepository;

import javax.ejb.Stateless;
import javax.inject.Inject;
import javax.security.enterprise.SecurityContext;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;

/**
 *
 * @author hantsy
 */
@Stateless
public class UserResource {

    @Context
    UriInfo uriInfo;

    @Inject
    UserRepository users;

    @Inject
    SecurityContext securityContext;

    @PathParam("username")
    String username;

    @GET
    public Response get() {

        return users.findByUsername(username)
            .map(
                u -> Response.ok(u)
                    .link(uriInfo.getBaseUriBuilder().path("users/{username}").build(username), "self")
                    .build()
            )
            .orElse(Response.status(Response.Status.NOT_FOUND).build());
    }

    @PUT
    public Response update(UserForm form) {

        // only a user himself  can edit his profile.
        if (securityContext.getCallerPrincipal() != null
            && securityContext.getCallerPrincipal().getName().equals(username)) {
            return users.findByUsername(username)
                .map(
                    u -> {
                        u.setFirstName(form.getFirstName());
                        u.setLastName(form.getLastName());
                        u.setEmail(form.getEmail());

                        users.save(u);
                        return Response.noContent().build();
                    }
                )
                .orElse(Response.status(Response.Status.NOT_FOUND).build());
        }

        return Response.status(Response.Status.UNAUTHORIZED).build();
    }

    @DELETE
    public Response delete() {

        return users.findByUsername(username)
            .map(
                u -> {
                    users.delete(u);
                    return Response.noContent().build();
                }
            )
            .orElse(Response.status(Response.Status.NOT_FOUND).build());
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/java/com/example/interfaces/user/UsersResource.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.interfaces.user;


import com.example.domain.task.Count;
import com.example.domain.task.Existence;
import com.example.domain.user.User;
import com.example.domain.user.UserRepository;
import com.example.application.util.hash.Crypto;
import com.example.application.util.hash.PasswordEncoder;

import javax.ejb.Stateless;
import javax.inject.Inject;
import javax.ws.rs.*;
import javax.ws.rs.container.ResourceContext;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;

import static com.example.application.util.hash.Crypto.Type.BCRYPT;
import static javax.ws.rs.core.Response.Status.BAD_REQUEST;
import static javax.ws.rs.core.Response.*;

/**
 * @author hantsy
 */
@Path("users")
@Stateless
@Produces(MediaType.APPLICATION_JSON)
public class UsersResource {

    @Context
    UriInfo uriInfo;

    @Inject
    UserRepository users;

    @Context
    ResourceContext resourceContext;

    @Inject
    @Crypto(BCRYPT)
    PasswordEncoder passwordEncoder;

    @GET
    public Response all() {
        return ok(users.findAll()).build();
    }

    @GET
    @Path("count")
    public Response count() {
        return ok(
                Count.builder().count(users.countAll()).build()
        ).build();
    }

    @GET
    @Path("exists")
    public Response exists(@QueryParam("username") String username, @QueryParam("email") String email) {
        if (username != null && username.length() > 0) {
            return ok(Existence.builder().existed(users.findByUsername(username).isPresent()).build()).build();
        }

        if (email != null && email.length() > 0) {
            return ok(Existence.builder().existed(users.findByEmail(email).isPresent()).build()).build();
        }

        return status(BAD_REQUEST)
                .entity("username or email query params is required")
                .build();
    }

    @POST
    // there is a bug when adding @Valid to request form data
    // https://github.com/javaee/glassfish/issues/22317
    public Response createUser(RegisterForm form) {

        if (users.findByUsername(form.getUsername()).isPresent()) {
            throw new UsernameWasTakenException(form.getUsername());
        }

        if (users.findByEmail(form.getEmail()).isPresent()) {
            throw new EmailWasTakenException(form.getEmail());
        }

        User user = User.builder()
                .username(form.getUsername())
                .password(passwordEncoder.encode(form.getPassword()))
                .firstName(form.getFirstName())
                .lastName(form.getLastName())
                .email(form.getEmail())
                .build();

        User saved = users.save(user);
        return created(
                uriInfo.getBaseUriBuilder()
                        .path("users/{username}")
                        .build(saved.getUsername())
        )
                .build();
    }

    @Path("{username}")
    public UserResource user() {
        return resourceContext.getResource(UserResource.class);
    }

}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/liberty/config/server.xml
<?xml version="1.0" encoding="UTF-8"?>
<server description="new server">

    <!-- Enable features -->
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>

    <!-- This template enables security. To get the full use of all the capabilities, a keystore and user registry are required. -->

    <!-- For the keystore, default keys are generated and stored in a keystore. To provide the keystore password, generate an 
         encoded password using bin/securityUtility encode and add it below in the password attribute of the keyStore element. 
         Then uncomment the keyStore element. -->
    <!--
    <keyStore password=""/> 
    -->

    <!--For a user registry configuration, configure your user registry. For example, configure a basic user registry using the
        basicRegistry element. Specify your own user name below in the name attribute of the user element. For the password, 
        generate an encoded password using bin/securityUtility encode and add it in the password attribute of the user element. 
        Then uncomment the user element. -->
    <basicRegistry id="basic" realm="BasicRealm">
        <!-- <user name="yourUserName" password="" />  -->
    </basicRegistry>

    <!-- To access this server from a remote client add a host attribute to the following element, e.g. host="*" -->
    <httpEndpoint id="defaultHttpEndpoint"
                  httpPort="9080"
                  httpsPort="9443"/>

    <!-- Automatically expand WAR files and EAR files -->
    <applicationManager autoExpand="true"/>

    <!-- Derby Library Configuration -->
    <library id="derbyJDBCLib">
        <fileset dir="${shared.resource.dir}" includes="derby*.jar"/>
    </library>

    <!-- Datasource Configuration -->
    <!-- remove jndiName="" to serve java:comp/DefaultDataSource for Java EE 7 or above -->
    <dataSource id="DefaultDataSource">
        <jdbcDriver libraryRef="derbyJDBCLib"/>
        <properties.derby.embedded databaseName="taskdb" createDatabase="create"/>
    </dataSource>

</server>
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/microprofile-config.properties
jwt.secretKey=rzxlszyykpbgqcflzxsqcysyhljt
# one day
jwt.tokenValidityInSeconds=86400
# 14 days
jwt.remembermeValidityInSeconds=1209600

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/orm.xml
<?xml version="1.0" encoding="UTF-8"?>
<entity-mappings xmlns="http://xmlns.jcp.org/xml/ns/persistence/orm"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence/orm http://xmlns.jcp.org/xml/ns/persistence/orm_2_1.xsd"
                 version="2.1">
    <persistence-unit-metadata>
        <persistence-unit-defaults>
            <entity-listeners>
                <entity-listener class="com.example.domain.common.AuditingEntityListener"/>
            </entity-listeners>
        </persistence-unit-defaults>
    </persistence-unit-metadata>
</entity-mappings>


--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/resources/META-INF/persistence.xml
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.2" xmlns="http://xmlns.jcp.org/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence http://xmlns.jcp.org/xml/ns/persistence/persistence_2_2.xsd">
  <persistence-unit name="defaultPU" transaction-type="JTA">
    <jta-data-source>java:comp/DefaultDataSource</jta-data-source>
    <exclude-unlisted-classes>false</exclude-unlisted-classes>
    <properties>
      <property name="javax.persistence.schema-generation.database.action" value="drop-and-create"/>
      <property name="hibernate.enable_lazy_load_no_trans" value="true" />
    </properties>
  </persistence-unit>
</persistence>

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/beans.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/beans_2_0.xsd"
       bean-discovery-mode="annotated"
       version="2.0">
</beans>
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/glassfish-web.xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
    DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
    Copyright (c) 2015-2017 Oracle and/or its affiliates. All rights reserved.
    The contents of this file are subject to the terms of either the GNU
    General Public License Version 2 only ("GPL") or the Common Development
    and Distribution License("CDDL") (collectively, the "License").  You
    may not use this file except in compliance with the License.  You can
    obtain a copy of the License at
    https://oss.oracle.com/licenses/CDDL+GPL-1.1
    or LICENSE.txt.  See the License for the specific
    language governing permissions and limitations under the License.
    When distributing the software, include this License Header Notice in each
    file and include the License file at LICENSE.txt.
    GPL Classpath Exception:
    Oracle designates this particular file as subject to the "Classpath"
    exception as provided by Oracle in the GPL Version 2 section of the License
    file that accompanied this code.
    Modifications:
    If applicable, add the following below the License Header, with the fields
    enclosed by brackets [] replaced by your own identifying information:
    "Portions Copyright [year] [name of copyright owner]"
    Contributor(s):
    If you wish your version of this file to be governed by only the CDDL or
    only the GPL Version 2, indicate your decision by adding "[Contributor]
    elects to include this software in this distribution under the [CDDL or GPL
    Version 2] license."  If you don't indicate a single choice of license, a
    recipient has the option to distribute your version of this file under
    either the CDDL, the GPL Version 2 or to extend the choice of license to
    its licensees as provided above.  However, if you add GPL Version 2 code
    and therefore, elected the GPL Version 2 license, then the option applies
    only if the new code is made subject to such option by the copyright
    holder.
-->

<!DOCTYPE glassfish-web-app PUBLIC "-//GlassFish.org//DTD GlassFish Application Server 3.1 Servlet 3.0//EN" "http://glassfish.org/dtds/glassfish-web-app_3_0-1.dtd">
<glassfish-web-app>

    <security-role-mapping>
        <role-name>ROLE_ADMIN</role-name>
        <group-name>ROLE_ADMIN</group-name>
    </security-role-mapping>
    
    <security-role-mapping>
        <role-name>ROLE_USER</role-name>
        <group-name>ROLE_USER</group-name>
    </security-role-mapping>

    <parameter-encoding default-charset="UTF-8" />

</glassfish-web-app>
--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/main/webapp/WEB-INF/web.xml
<?xml version="1.0" encoding="UTF-8"?>

<web-app
    xmlns="http://xmlns.jcp.org/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
    version="4.0"
>
    <!-- Security constraints  -->
    <security-constraint>
        <web-resource-collection>
            <web-resource-name>Protected resource/url</web-resource-name>
            <url-pattern>/api/tasks/*</url-pattern>
            <url-pattern>/api/users/*</url-pattern>
            <http-method>POST</http-method>
            <http-method>PUT</http-method>
            <http-method>DELETE</http-method>
        </web-resource-collection>
        <auth-constraint>
            <role-name>ROLE_USER</role-name>
            <role-name>ROLE_ADMIN</role-name>
        </auth-constraint>
    </security-constraint>
    <security-constraint>
        <web-resource-collection>
            <web-resource-name>Current user resource/url</web-resource-name>
            <url-pattern>/api/me/*</url-pattern>
        </web-resource-collection>
        <auth-constraint>
            <role-name>ROLE_USER</role-name>
            <role-name>ROLE_ADMIN</role-name>
        </auth-constraint>
    </security-constraint>
</web-app>

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/.gitkeep

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/it/TaskRepositoryTest.java
package com.example.it;

import com.example.domain.common.AbstractEntity;
import com.example.domain.task.TaskRepository;
import com.example.domain.task.Task;
import com.example.infrastructure.persistence.jpa.AbstractRepository;
import com.example.infrastructure.persistence.jpa.JpaTaskRepository;
import org.jboss.arquillian.container.test.api.Deployment;
import org.jboss.arquillian.junit.Arquillian;
import org.jboss.shrinkwrap.api.ShrinkWrap;
import org.jboss.shrinkwrap.api.spec.JavaArchive;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

import javax.inject.Inject;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.logging.Level;
import java.util.logging.Logger;

import static org.junit.Assert.assertEquals;

@RunWith(Arquillian.class)
public class TaskRepositoryTest {
    private static final Logger LOGGER = Logger.getLogger(TaskRepositoryTest.class.getName());

    @Deployment()
    public static JavaArchive createDeployment() {
        JavaArchive jar = ShrinkWrap.create(JavaArchive.class)
                .addPackage(AbstractEntity.class.getPackage())
                .addPackage(Task.class.getPackage())
                .addClass(JpaTaskRepository.class).addClass(AbstractRepository.class)
                //Add JPA persistence configuration.
                //WARN: In a jar archive, persistence.xml should be put into /META-INF
                .addAsManifestResource("META-INF/persistence.xml", "persistence.xml");

        LOGGER.log(Level.INFO, "deployment unit: {0}", jar);

        return jar;
    }

    @Inject
    TaskRepository tasks;

    @PersistenceContext
    EntityManager em;

    Task saved;

    @Before
    public void setup() {
        saved = tasks.save(Task.of("test task", "desc of test task"));
    }

    @After
    public void teardown() {

    }

    @Test
    public void shouldCreated() {
        Task found = em.find(Task.class, saved.getId());

        assertEquals("name is 'test task'", "test task", found.getName());
        assertEquals("description is 'desc of test task'", "desc of test task", found.getDescription());
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/java/com/example/it/TaskResourceTest.java
package com.example.it;

import com.example.application.util.SampleDataPopulator;
import com.example.domain.common.AbstractEntity;
import com.example.domain.task.Task;
import com.example.domain.user.User;
import com.example.infrastructure.persistence.jpa.AbstractRepository;
import com.example.infrastructure.persistence.jpa.JpaTaskRepository;
import com.example.infrastructure.persistence.jpa.JpaUserRepository;
import com.example.interfaces.RestConfiguration;
import com.example.interfaces.common.PageParam;
import com.example.interfaces.common.PagedResult;
import com.example.interfaces.task.TaskResources;
import org.jboss.arquillian.container.test.api.Deployment;
import org.jboss.arquillian.junit.Arquillian;
import org.jboss.arquillian.test.api.ArquillianResource;
import org.jboss.shrinkwrap.api.ShrinkWrap;
import org.jboss.shrinkwrap.api.asset.EmptyAsset;
import org.jboss.shrinkwrap.api.spec.WebArchive;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.GenericType;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

import static org.junit.Assert.assertTrue;

@RunWith(Arquillian.class)
public class TaskResourceTest {
    private static final Logger LOGGER = Logger.getLogger(TaskResourceTest.class.getName());
    
    @Deployment(testable = false)
    public static WebArchive createDeployment() {
        WebArchive war = ShrinkWrap.create(WebArchive.class)
                
                // entities
                .addPackage(AbstractEntity.class.getPackage())
                .addPackage(Task.class.getPackage())
                .addPackage(User.class.getPackage())
                .addClass(JpaTaskRepository.class).addClass(JpaUserRepository.class).addClass(AbstractRepository.class)
                
                //sample data
                .addPackages(true, SampleDataPopulator.class.getPackage())
                
                // rest
                .addPackage(TaskResources.class.getPackage())
                .addPackage(PageParam.class.getPackage())
        
                //rest config
                .addClass(RestConfiguration.class)
                
                //Add JPA persistence configuration.
                //WARN: In a war archive, persistence.xml should be put into /WEB-INF/classes/META-INF/, not /META-INF
                .addAsResource("META-INF/persistence.xml", "META-INF/persistence.xml")
                // Enable CDI
                .addAsWebInfResource(EmptyAsset.INSTANCE, "beans.xml");
        
        LOGGER.log(Level.INFO, "deployment unit: {0}", war);
        
        return war;
    }
    
    @ArquillianResource
    private URL base;
    
    private Client client;
    
    @Before
    public void setup() {
        this.client = ClientBuilder.newClient();
    }
    
    @After
    public void teardown() {
        if (this.client != null) {
            this.client.close();
        }
    }
    
    @Test
    public void shouldFoundTasks() throws MalformedURLException {
        final WebTarget getAllTasksTarget = client.target(URI.create(new URL(base, "api/tasks").toExternalForm()));
        try (final Response getAllTasksResponse = getAllTasksTarget.request()
                .accept(MediaType.APPLICATION_JSON)
                .get()) {
            assertTrue("status is ok", getAllTasksResponse.getStatus() == 200);
            assertTrue("response should contain two tasks",
                    getAllTasksResponse.readEntity(new GenericType<PagedResult<Task>>() {
                    }).getContent().size() == 2);
            
        }
    }
}

--#

--% /tmp/hapus/jakartaee/jakartaee-jaxrs-sample/src/test/resources/arquillian.xml
<arquillian xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://jboss.org/schema/arquillian"
            xsi:schemaLocation="http://jboss.org/schema/arquillian
    http://jboss.org/schema/arquillian/arquillian_1_0.xsd">
    <defaultProtocol type="Servlet 3.0"/>
    <container qualifier="glassfish" default="true">
        <configuration>
            <property name="domain">domain1</property>
            <property name="adminUser">admin</property>
            <property name="adminPassword"></property>
        </configuration>
    </container>
</arquillian>
--#

