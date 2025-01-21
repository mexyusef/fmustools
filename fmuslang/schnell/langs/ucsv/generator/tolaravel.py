from anytree import Node, AnyNode, RenderTree, AsciiStyle, PreOrderIter
from anytree.importer import JsonImporter, DictImporter

sequelize_type_mapper = {
	'string':       '$table->string', # $table->string('name', 100)
	'text':         '$table->text',
	'integer':      '$table->integer',
	'number':       '$table->decimal', # $table->decimal('amount', 5, 2);
	'bigint':       '$table->bigInteger',
	'ubigint':      '$table->unsignedBigInteger',
	'smallint':     '$table->smallInteger',
	'tinyint':      '$table->tinyInteger',
	'boolean':      '$table->boolean',
	'date':         '$table->date',
	'datetime':     '$table->dateTime',
	'time':         '$table->time',
	'float':        '$table->float',
	'double':       '$table->double',
	'timestamp':    '$table->timestamp',	
	'enum':         '$table->enum', 
	# $table->enum('choices', array('foo', 'bar'));
	# $table->enum('role', ['admin','author','subscriber'])->default('author');
	# laravel
	'timestamps':   '$table->timestamps()',
	# perlu ada bbrp jenis id: id, idi, idbi
	'id':           '', # $table->id(), $table->bigIncrements('id'); $table->increments('id');
}

# constraints
# $table->primary('id');
# $table->primary(array('first', 'last')); 
# $table->foreign('user_id')->references('id')->on('users'); <- current.user_id = users.id
# $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
# $table->foreign('author_id')->references('id')->on('users')->onDelete('cascade');

# $table->foreign('on_post')
# ->references('id')->on('posts')
# ->onDelete('cascade');

# $table->foreign('from_user')
# ->references('id')->on('users')
# ->onDelete('cascade');

# ->default($value)
# ->nullable()
# ->unsigned()
# $table->unique('email');
# $table->index('state');

model = []

pre_prefix = """<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class __TABLENAME_PLURAL_TITLED__ extends Migration
{
	public function up()
	{
"""

post_suffix = """
	}

	public function down()
	{
		Schema::drop('__TABLENAME_PLURAL_LOWER__');
	}
"""

sample_model = """
<?php

namespace App;
use Illuminate\Database\Eloquent\Model;

class __TABLENAME_PLURAL_TITLED__ extends Model
{
	protected $guarded = [];
	
	public function other_model_that_we_owned()
	{
		return $this->hasMany('App\\__OTHER_MODEL_OWNED__', '__OTHER_MODEL_OWNED_COLUMN__')
	}
	public function other_model_that_owns_us()
	{
		return $this->belongsTo('App\\__OTHER_MODEL_OWNER__', 'column_on_owner')
	}
}
"""

sample_controller = """
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
class __OUR_VALIDATION_CLASS__ extends FormRequest
{
	public function authorize()
	{
		if ($this->user()->can_post())
			return true;
		return false;
	}

	public function rules()
	{
		return [
			'title' => 'required | unique:posts | max:255',
			'title' => array('Regex:/^[A-Za-z0-9 \.,:)]+$/'),
			'body' => 'required',
		];
	}
}

<?php

namespace App\Http\Controllers;

use Illuminate\Support\Str;
use Illuminate\Http\Request;

use App\Http\__OUR_VALIDATION_CLASS__;
use App\__TABLENAME_TITLED__;

class __TABLENAME_TITLED__Controller extends Controller
{
	public function list()
	{
		$__TABLENAME_PLURAL_LOWER__ = __TABLENAME_PLURAL_TITLED__
			::where('active', 1)
			->orderBy('created_at', 'desc')
			->paginate(5);
		$title = 'Latest __TABLENAME_PLURAL_TITLED__';
		return view('home')
			->withPosts($__TABLENAME_PLURAL_LOWER__)
			->withTitle($title);
	}

	public function detail($slug)
	{
		$__TABLENAME_LOWER__ = __TABLENAME_PLURAL_TITLED__
			::where('slug', $slug)
			->first();
		if (!$__TABLENAME_LOWER__)
			return redirect('/')
				->withErrors('requested page not found');

		$comments = $__TABLENAME_LOWER__->comments;
		return view('__TABLENAME_PLURAL_LOWER__.show')
			->withPost($__TABLENAME_LOWER__)
			->withComments($comments);
	}

	public function create_view(Request $request)
	{
		if ($request->user()->can_post())
			return view('__TABLENAME_PLURAL_LOWER__.create');
		else
			return redirect('/')->withErrors('Cannot get create view.');
	}

	public function create(__OUR_VALIDATION_CLASS__ $request)
	{
		$__TABLENAME_LOWER__ = new __TABLENAME_PLURAL_TITLED__();
		$__TABLENAME_LOWER__->title = $request->get('title');
		$__TABLENAME_LOWER__->body = $request->get('body');
		$__TABLENAME_LOWER__->slug = Str::slug($__TABLENAME_LOWER__->title);
		
		$duplicate = __TABLENAME_PLURAL_TITLED__
			::where('slug', $__TABLENAME_LOWER__->slug)
			->first();
		
		if ($duplicate) {
			// Route::get('new-post', 'ModelController@create_view');
			return redirect('new-post')
				->withErrors('Title already exists.')
				->withInput();
		}

		$__TABLENAME_LOWER__->author_id = $request->user()->id;
		
		if ($request->has('save')) {
			// <input type="submit" name='save' class="btn btn-default" value = "Save Draft" />
			$__TABLENAME_LOWER__->active = 0;
			$message = 'Resource saved successfully';
		} else {
			// <input type="submit" name='publish' class="btn btn-success" value = "Publish"/>
			$__TABLENAME_LOWER__->active = 1;
			$message = 'Resource published successfully';
		}
		
		$__TABLENAME_LOWER__->save();
      	return redirect('edit/' . $__TABLENAME_LOWER__->slug)
		  	->withMessage($message);
	}

	public function update(Request $request)
	{
		$__TABLENAME_LOWER__ = __TABLENAME_PLURAL_TITLED__
			::where('slug', $slug)
			->first();
		if ($__TABLENAME_LOWER__ && 
			(
				$request -> user() -> id == $__TABLENAME_LOWER__ -> author_id 
				|| 
				$request->user() -> is_admin())
			)
			return view('__TABLENAME_LOWER__.edit')
				->with('__TABLENAME_LOWER__', $__TABLENAME_LOWER__);

		return redirect('/')->withErrors('Cannot update.');
	}

	public function destroy(Request $request, $id)
	{
		$__TABLENAME_LOWER__ = __TABLENAME_PLURAL_TITLED__
			::find($id);
		if ($__TABLENAME_LOWER__ && 
			(
				$__TABLENAME_LOWER__ -> author_id == $request->user() -> id 
				|| 
				$request -> user() -> is_admin()
			)
		)
		{
			$__TABLENAME_LOWER__->delete();
			$data['message'] = '__TABLENAME_TITLED__ deleted.';
		}
		else
		{
			$data['errors'] = 'Delete failed.';
		}
		return redirect('/')
			->with($data);
	}
}

"""

def create_model():
	return sample_model

def to_laravel(RootNode):
	print(f"---------------------------------{__file__}-------------------------------")
	print(f"root: {RootNode}, initial result: {model}")
	if not hasattr(RootNode, 'model'):
		print('set nama model/table singular/lower pada configuration, misal {laravel@post}...')
		return ''

	for column in PreOrderIter(RootNode):
		if column.type != 'root':
			if hasattr(column, 'hasConstraint') and column.hasConstraint == True: # complex type {}
				kolom_model = ''

				default_get_type = sequelize_type_mapper[column.type]
				kolom_model += default_get_type + f"('{column.label}')"
				# if column.type == 'varchar' and hasattr(column, 'typenum'):
				# 	default_get_type += f'({column.typenum})'
				if hasattr(column, 'unique'):
					kolom_model += '->unique()'
				if hasattr(column, 'allowNull'):
					kolom_model += '->nullable()'
				if hasattr(column, 'defaultValue'):
					kolom_model += f"->default('{column.defaultValue}')"
				# if hasattr(column, 'referencesKey'):
				# 	replacement = column.referencesKey.replace(QuoteChar, ReplaceQuoteChar)
				# 	model[column.label] .update({ 'referencesKey': replacement })
				if hasattr(column, 'primaryKey'):
					if hasattr(column, 'pk'):
						if len(column.pk) == 1:
							model .append(f"$table->primary('{column.pk[0]}')")
						else:
							quoted_pk = ["'"+item+"'" for item in column.pk]
							col_list = ', '.join(quoted_pk)
							pk = f"$table->primary(array({col_list}))"
							model .append(pk)
					else: # berarti current label jadi primary key
						model .append(f"$table->primary('{column.label}')")
				if hasattr(column, 'foreignKey'):
					# $table->foreign('author_id')->references('id')->on('users')->onDelete('cascade');
					operation = ''
					if hasattr(column, 'fk_action'):
						operation1 = []
						# print('oprek fk_action')
						for k,v in column.fk_action.items():
							if k == 'delete_action':
								operation1.append(f"->onDelete('{v}')")
							elif k == 'update_action':
								operation1.append(f"->onUpdate('{v}')")
						operation = ''.join(operation1)

					fk = f"$table->foreign('{column.label}')->references('{column.fk_column}')->on('{column.fk_table}'){operation}"
					# kolom_model = fk
					model .append(fk)
				
				if kolom_model != '': # proses model.append di atas akan hasilkan kolom_model=''
					model .append(kolom_model)
			elif column.type == 'index':
				generated = '$table->'
				if hasattr(column, 'index_unique') and column.index_unique:
					generated += "unique('"
				else:
					generated += "index('"
				generated += column.label + "')"
				model .append(generated)

			else: # simple type
				default_get_type = sequelize_type_mapper[column.type]
				kolom_model = default_get_type + f"('{column.label}')"
				# if column.type == 'varchar' and hasattr(column, 'typenum'):
				# 	default_get_type += f'({column.typenum})'
				model .append(kolom_model)

	model .append('// --------------------------')
	model .append('$table->id()')
	model .append("$table->bigIncrements('id')")
	model .append("$table->increments('id')")
	model .append('$table->timestamps()')
	model .append('// --------------------------')
	mvc = sample_model
	mvc += sample_controller
	prefix = mvc + pre_prefix + "Schema::create('__TABLENAME__', function (Blueprint $table) {\n"
	suffix = "\n});" + post_suffix
	result = prefix + ';\n'.join(['\t'+item for item in model]) + suffix
	result = result \
		.replace('__TABLENAME_TITLED__', RootNode.model.title()) \
		.replace('__TABLENAME_PLURAL_TITLED__', (RootNode.model + 's').title()) \
		.replace('__TABLENAME_LOWER__', RootNode.model.lower()) \
		.replace('__TABLENAME_PLURAL_LOWER__', (RootNode.model + 's').lower()) \
		.replace('__TABLENAME__', (RootNode.model + 's').lower())

	return result
