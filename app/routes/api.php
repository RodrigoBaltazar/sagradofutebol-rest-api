<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Resources\PlaysResource;
use App\Models\Play;
use App\Http\Controllers\api\PlayController;


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

Route::get('/play', [PlayController::class, 'store']);

Route::get('/plays/{id}', [PlayController::class, 'show']);

Route::put('/plays/{id}', [PlayController::class, 'update']);

Route::delete('/plays/{id}', [PlayController::class, 'destroy']);