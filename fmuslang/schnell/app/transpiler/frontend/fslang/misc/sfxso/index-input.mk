--% index/fmus
sfxso,d(/mk)
  # %template=/home/usef/danger/ulib/upy/ulibpy/compete/programs/templates/gui/scalafx dailymail stage1
  # %asset=/home/usef/danger/ulib/upy/ulibpy/compete/projects/scalafx/starterapp2

  build.sbt,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=build.sbt)
	README.md,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=rujukan)

  project,d(/mk)
    build.properties,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/res.mk=/project/build.properties)
  
  #manual copy gara2 gak kuasai sbt...
  target,d(/mk)
    scala-2.13,d(/mk)
      classes,d(/mk)
        be,d(/mk)
          fulgent,d(/mk)
            scalafx,d(/mk)
              ui,d(/mk)
                Program.css,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=Program.css)
                images,d(/mk)
                  paper.png,f(b64=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/res.mk=paper.png)

  src,d(/mk)
    main,d(/mk)
      scala,d(/mk)
        be,d(/mk)
          fulgent,d(/mk)
            scalafx,d(/mk)
              model,d(/mk)
                Model.scala,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=Model.scala)
              ui,d(/mk)                
                Program.scala,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=Program.scala/main)
      resources,d(/mk)
        Program.css,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/code.mk=Program.css)
        images,d(/mk)
          paper.png,f(b64=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/sfxso/res.mk=paper.png)

  #$code .
  #$sbt run
  #@jalankan sbt run
  #$x-terminal-emulator &
	$* cmd.exe /c start "sbt run"
--#

