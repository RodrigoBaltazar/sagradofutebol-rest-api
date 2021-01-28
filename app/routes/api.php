<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Resources\PlaysResource;
use App\Models\Play;
use App\Http\Controllers\api\PlayController;
use App\Http\Controllers\PlayStreamController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/plays', [PlayController::class, 'index']);

Route::POST('/play', [PlayController::class, 'store']);

Route::get('/plays/{id}', [PlayController::class, 'show']);

Route::put('/plays/{id}', [PlayController::class, 'update']);

Route::delete('/plays/{id}', [PlayController::class, 'destroy']);

Route::post('/stream/on_publish', [PlayStreamController::class, 'on_publish']);




Route::get('plays/midia/{filename}', function ($filename) {
    // Pasta dos videos.
    $videosDir = base_path('storage/app/');

    if (file_exists($filePath = $videosDir."/".$filename)) {
        $stream = new PlayStreamController($filePath);

        return response()->stream(function() use ($stream) {
            $stream->start();
        });
    }

    return response("File doesn't exists", 404);
});