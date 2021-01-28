@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Dashboard') }}</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif
                    <form method="POST" action="{{route('PlayController@store')}}" accept-charset="UTF-8">
                        <input name="_token" type="hidden" value="{{ csrf_token() }}"/>
                        <div>
                            <label for="Title">Title:</label>
                            <input type="text" name="title" />
                        </div>
                        <div>
                            <label for="Path">Path:</label>
                            <input type="text" name="path" />
                        </div>
                        <div>
                            <label for="File">File:</label>
                            <input type="file" name="play" />
                        </div>
                        <input type="submit">
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
