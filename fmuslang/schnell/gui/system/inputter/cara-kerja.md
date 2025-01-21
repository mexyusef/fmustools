
tiap plugins menerima cmd/keyword
\r      Run
\g      Go

Run(worker=worker, client=client) <- kita assign worker dan client...

self.plugins = {
    'r':        plugin Run,
}
self.default_plugin = plugins[0] if self.plugins else None
plugin pertama adlh default plugin

def query():
    jk cmd (r) ada di self.plugins, maka plugin = self.plugins[cmd]
    plugin.worker.clear()
    plugin.lit(
        arg,
        upper_bound=MAX_LIST_LENGTH,
        finished=self._try_popup
    )
plugin.lit tentu ngarah ke method lit() dari Run...yg adlh Files...
kita lihat Files.lit():
    def lit(self, query, upper_bound, finished, *args, **kargs):
        self.worker.do(job=Job(self, query, upper_bound, finished))
        ^ utk \r ini kargs adlh job=...
ternyata plugin lit() ini menyuruh kerja ke worker utk do()

# worker.do(), cek Make, Action, atau Job...JAM stack?
so lihat apa do() dari worker?
        if 'make' in kargs: # ini utk \g
            make = kargs['make']
            catch = kargs.get('catch', lambda x: x)
            job = Make(
                make,
                catch,
                main=kargs.get('main', False),
                priority=kargs.get('priority', 0)
            )
        elif 'action' in kargs:
            action = kargs['action']
            react = kargs.get('react', lambda: None)
            job = Action(
                action,
                react,
                main=kargs.get('main', False),
                priority=kargs.get('priority', 0)
            )
        elif 'job' in kargs: # ini utk \r
            job = kargs['job']
            _check_job(job)
        self.q.push(job, -_getattr(job, 'priority', 0))
        self.delay_deal()
ternyata: Make(...) utk \g, eh job.run() atau self.pool.start(job) utk \r

# mengenai Job.run()
kita lihat gimana sih Job run() itu:
            for runnable in self.p.d.values():
                runnable.query.update(self.query.lower())

            def f(runnable):
                """Don't calculate editing distance if job stopped."""
                if self.canceled:
                    return 0
                elif not self.query:
                    return runnable.order
                else:
                    return runnable.query.distance_to(runnable.name.lower())

            QMetaObject.invokeMethod(
                self,
                '_make_model',
                Qt.QueuedConnection,
                Q_ARG(object, sorted(self.p.d.values(), key=f)[:self.upper_bound])
            )

    @pyqtSlot(object)
    def _make_model(self, args):
        if not self.canceled:
            with QMutexLocker(self.mutex):
                self.finished(RunnableModel(args)) <= apakah ini bikin completer?
        self.deleteLater()
jadi:
plugin lit() => worker do() => Job run()
                               ^ utk \r 

# siapakah self.impl?
self.impl ada di Make dan Action
bgm utk job?
di Job2 di Pool di Worker...ada self.impl.run()

self.impl adlh Make, Action, dan (Files) Job yg punya method run.
tapi Make sendiri terima impl...jd Make bukan impl dong?

ok coba begini bedakannya
Go v Worker
Go punya lit, yg manggil worker.do(make=...)
di sini make=... adlh impl yg sebenarnya
dia adlh fungsi yg kembalikan WindowModel()
jadi Worker/Make itu tepatnya "impl wrapper"
utk Make dan Action, "impl wrapper" punya run()
tapi utk job, yg impl = wrapper, maka Job punya run() sendiri => spt di Files/Job.

coba lihat utk Go Worker Make, ini adlh hasil dari make impl:
active_tasks = [self.tasks[h] for h in hwnds]
return [task for i, task in sorted(enumerate(active_tasks), key=lambda i: ds[i[0]])]
utk task, title dan name adlh judul dari window hwnd.

# siapa yg kasih result?
dari Run, __init__, kita kumpulkan semua *.exe dll stlh selesai kita aktikfan signal Files/path_list_changed
dari Files kita lihat ada path_list_changed mengisi self.d = dict(runnables) krn runnables itu [ (name, Runnable()) ]
di sini artinya apa? result terbentuk di sini...dg key = name dari file *.exe dsb tanpa extension.

kita lihat di Job/run() (nanti terlihat self.p = parent dari Job = Files)
for runnable in self.p.d.values():
    runnable.query.update(self.query.lower())
di sini, self.p.d...artinya self.p itu adlh Run/Files yg punya self.d = dictionary of content/result utk popup box

kt lihat __init__ dari job:
Job
    def __init__(self, p, query, upper_bound, finished):
        super(Job, self).__init__()
        self.p = p
Files
    def lit(self, query, upper_bound, finished, *args, **kargs):
        self.worker.do(job=Job(self, query, upper_bound, finished))

                               (kita tau query = args wkt \r args)
                               (kita jg tau, finished itu popup yg nampilkan dialog dan nerima content)

                               Files, query, upper_bound, finished
                               diterima di job:
                               p,     query, upper_Bound, finished

jadi self.p itu = self.parent maksudnya, parent dari Job adlh Files.

# files select(), yg lakukan/exec \r
win32api.ShellExecute(0, 'open', self.d[name].path, '', '', 1)

# Job _make_model
    @pyqtSlot(object)
    def _make_model(self, args):
        if not self.canceled:
            with QMutexLocker(self.mutex):
                self.finished(RunnableModel(args))
        self.deleteLater()
.

# big question: gimana bikin plugin sendiri?
tapi apa yg pengen kita lakukan?
kita cuma pengen keluarkan tampilan...

C:\work\oprek\kerja\lit
kita hrs lihat, jk kita pengen Action...
jd gimana?
kan pengen actionnya adlh tampilkan hasil get definition dari mk/fmus

# recap

dari worker, cek apa dia dari (atau minta): make (\g), action (\exit), job (\r)
    perlu ingat bhw make dan action adlh impl
tapi make dan action ini mirip.
terima 
    impl = main process
    finished = callback stlh selesai
    failed = None, callback jk gagal
    main = True or False, main thread atau bukan
    priority
.
baik make dan action punya run yg berisi: impl() lalu finished()

worker punya self.q utk queue job.
lalu stlh push ke self.q, dia "deal" dg panggil job.run() atau self.pool.start(job)
akhirnya, cek lagi jk masih ada isi self.q maka "deal" secara rekursif.

# act vs select utk Go / Make
yg dipanggil select wkt model diactivated
tapi ada jg pemanggil act() dimana tuh
    def act(self):
        if self.cmd == 'exit':
            self._teardown_plugins()
            self.client.stop()
            QApplication.quit()
        if self.cmd in self.plugins:
            self.plugins[self.cmd].act()
spt nya ini hanya utk action deh???
bukan utk make dan job...
