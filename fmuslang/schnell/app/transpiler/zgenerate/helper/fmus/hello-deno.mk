--% program/fmus
/tmp/hapus/hello-deno,d(/mk)
	hello.ts,f(e=__FILE__=hello.ts)
	work.fmus,f(e=__FILE__=work.fmus)
	run.sh,f(e=__FILE__=run.sh)
	$*chmod a+x *.sh
	$*code .
--#

--% hello.ts
import { serve } from "https://deno.land/std@0.83.0/http/server.ts";
for await (const req of serve(":8080")) {
  req.respond({ body: "Hello deno" });
}
--#

--% work.fmus
term
--#

--% run.sh
deno run --allow-net hello.ts
--#
